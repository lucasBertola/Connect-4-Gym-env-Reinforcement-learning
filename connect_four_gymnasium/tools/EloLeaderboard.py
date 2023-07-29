import math
import sys
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
            AdultSmarterPlayer()
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
    
    def play_round(self, k_factor, player, actualElo):
        # Iterate through all possible player-opponent pairs
        for opponent in self.playersWithEloFixed:
            player_score = self.get_score(player, opponent)
            player_won = player_score > 0
            draw = player_score == 0
            opponent_elo = opponent.getElo()
            actualElo = self.update_elo(actualElo, opponent_elo, player_won, k_factor,draw)
        
        return actualElo

    def get_elo(self, player, num_matches=100,display_log=True):

        actualElo = player.getElo() if player.getElo() is not None else 1500
        
        # Play the specified number of matches
        for i in range(num_matches*2):
            k_factor = 32 / (1 + i / 10)
            actualElo = self.play_round(k_factor,player,actualElo)
            if display_log:
                print(f"Elo rankings after {i+1} matches: {actualElo}")

        return actualElo

    def get_score(self, player, opponent):
        # Initialize the game environment
        env = ConnectFourEnv(opponent=opponent)
        obs, _ = env.reset()
        # Play the game until it ends
        while True:
            action = player.play(obs)
            obs, rewards, dones, truncated, _ = env.step(action)
            if truncated or dones:
                obs, _ = env.reset()
                return rewards


if __name__ == "__main__":
    from connect_four_gymnasium.players import (MinMaxPlayer)

    elo_leaderboard = EloLeaderboard()
    print(elo_leaderboard.get_elo([MinMaxPlayer(depth=1)], num_matches=100))

# 1. AdultSmarterPlayer:    1767
# 2. AdultPlayer:           1712
# 3. MinimaxPlayer depth 3: 1672
# 4. MinimaxPlayer depth 2: 1622
# 5. TeenagerSmarterPlayer: 1611
# 6. TeenagerPlayer:        1604
# 7. ChildSmarterPlayer:    1525
# 8. MinimaxPlayer depth 1: 1220
# 9. ChildPlayer:           1208
# 10. BabyPlayer:            995