import math
import sys
import random
sys.path.append('../../')

from connect_four_gymnasium.ConnectFourEnv import ConnectFourEnv
from connect_four_gymnasium.players import (
    BabyPlayer,
    ChildPlayer,
    ChildSmarterPlayer,
    TeenagerPlayer,
    TeenagerSmarterPlayer,
    AdultPlayer,
    AdultSmarterPlayer,
)

class EloLeaderboard:
    def __init__(self):
        # Initialize the list of players
        self.playersWithEloFixed = [
            BabyPlayer(),
            ChildPlayer(),
            ChildSmarterPlayer(),
            TeenagerPlayer(),
            TeenagerSmarterPlayer(),
            AdultPlayer(),
            # AdultSmarterPlayer()
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
    
    def play_rounds(self, player, actualElo,num_matches):
        gamePlayed = 0
        all_match_opponents = [player for player in self.playersWithEloFixed for _ in range(num_matches)]
        random.shuffle(all_match_opponents)
        scores = self.get_scores(player, all_match_opponents)
        for opponent, score in zip(all_match_opponents, scores):
            player_won = score > 0
            draw = score == 0
            opponent_elo = opponent.getElo()
            k_factor = 32 / (1 + gamePlayed / 10)
            actualElo = self.update_elo(actualElo, opponent_elo, player_won, k_factor, draw)
            gamePlayed += 1

        return actualElo

    def get_elo(self, player, num_matches=400):
        actualElo = player.getElo() if player.getElo() is not None else 1500
        return self.play_rounds(player,actualElo,num_matches)

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
    from connect_four_gymnasium.players import (TeenagerSmarterPlayer)

    elo_leaderboard = EloLeaderboard()
    print(elo_leaderboard.get_elo([TeenagerSmarterPlayer()], num_matches=100))
