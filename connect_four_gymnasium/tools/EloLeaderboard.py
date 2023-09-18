import math
import sys
import random
sys.path.append('../../')

from connect_four_gymnasium.ConnectFourEnv import ConnectFourEnv
from connect_four_gymnasium.players import (
    BabyPlayer,
    BabySmarterPlayer,
    ChildPlayer,
    ChildSmarterPlayer,
    TeenagerPlayer,
    TeenagerSmarterPlayer,
    AdultPlayer,
    AdultSmarterPlayer,
    SelfTrained1Player,
    SelfTrained2Player,
    SelfTrained3Player,
    SelfTrained4Player,
    SelfTrained5Player,
    SelfTrained6Player,
    SelfTrained7Player,
)

class EloLeaderboard:
    def __init__(self):
        # Initialize the list of players
        self.playersWithEloFixed = [
            BabyPlayer(),
            BabySmarterPlayer(),
            ChildPlayer(),
            SelfTrained1Player(),
            ChildSmarterPlayer(),
            TeenagerPlayer(),
            TeenagerSmarterPlayer(),
            AdultPlayer(),
            AdultSmarterPlayer(),
            SelfTrained2Player(),
            SelfTrained3Player(),
            SelfTrained4Player(),
            SelfTrained5Player(),
            SelfTrained6Player(),  
            SelfTrained7Player(),  
        ]

    def update_elo(self, player_elo, opponent_elo, player_won, k_factor=32, draw=False):
        # Calculate the expected outcome based on the current Elo ratings
        expected_outcome = 1 / (1 + math.pow(10, (opponent_elo - player_elo) / 400))
        # Set the actual outcome based on whether the player won, lost, or drew
        if draw:
            actual_outcome = 0.5
        else:
            actual_outcome = 1 if player_won else 0
        # Update the player's Elo rating
        new_elo = player_elo + k_factor * (actual_outcome - expected_outcome)
        return new_elo

    def get_closest_opponents(self, player_elo, num_opponents=2):
        sorted_opponents = sorted(self.playersWithEloFixed, key=lambda opponent: abs(opponent.getElo() - player_elo))
        return sorted_opponents[:num_opponents]

    def play_rounds(self, player, actualElo, num_matches, parallel):
        gamePlayed = 0
        match_results = []
        num_matches = round(max(num_matches/10,1) if parallel else num_matches)
        for _ in range(num_matches):
            closest_opponents = self.get_closest_opponents(actualElo, num_opponents=2)
            if parallel:
                for _ in range(9):
                    resultat = self.get_closest_opponents(actualElo, num_opponents=2)
                    closest_opponents.extend(resultat)

            random.shuffle(closest_opponents)
            # scores =[True,True]# For finding the actual max elo 
            scores = self.get_scores(player, closest_opponents)
            for opponent, score in zip(closest_opponents, scores):
                player_won = score > 0
                draw = score == 0
                match_results.append((player_won, draw, opponent.getElo()))
                k_factor = 400 / (1 + (gamePlayed))
                actualElo = self.update_elo(actualElo, opponent.getElo(), player_won, k_factor, draw)
                gamePlayed += 1

        for _ in range(2000):
            for player_won, draw, opponent_elo in match_results:
                k_factor = 400 / (1 + (gamePlayed))
                actualElo = self.update_elo(actualElo, opponent_elo, player_won, k_factor, draw)
                gamePlayed += 1

        return actualElo

    def get_elo(self, player, num_matches=100,parallel=False):
        actualElo = player.getElo() if player.getElo() is not None else 1400
        return self.play_rounds(player, actualElo, num_matches,parallel)

    def get_scores(self, player, opponents):
        envs = [ConnectFourEnv(opponent=opponent) for opponent in opponents]
        obs_list = [obs for obs, _ in [env.reset() for env in envs]]
        scores = [0] * len(opponents)
        remaining_indices = list(range(len(opponents)))

        while remaining_indices:
            actions = player.play([obs_list[i] for i in remaining_indices])
            new_remaining_indices = []

            for i, action in zip(remaining_indices, actions):
                obs, rewards, dones, truncated, _ = envs[i].step(action)
                if truncated or dones:
                    obs_list[i], _ = envs[i].reset()
                    scores[i] = rewards
                else:
                    obs_list[i] = obs
                    new_remaining_indices.append(i)

            remaining_indices = new_remaining_indices

        return scores

if __name__ == "__main__":
    import time
    elo_leaderboard = EloLeaderboard()
    start_time = time.time()
    print(elo_leaderboard.get_elo(SelfTrained6Player(), num_matches=500,parallel=True))
    end_time = time.time()
    print(f"Time elapsed: {end_time - start_time} seconds")