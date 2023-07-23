import math
import sys
sys.path.append('../../')

from connect_four_gymnasium.ConnectFourEnv import ConnectFourEnv


class EloLeaderboard:
    def __init__(self, players):
        self.players = players
        self.elo_rankings = {player.getName(): 1500 for player in players}

    def update_elo(self, player_elo, opponent_elo, player_won, k_factor=32):
        expected_outcome = 1 / (1 + math.pow(10, (opponent_elo - player_elo) / 400))
        actual_outcome = 1 if player_won else 0
        new_elo = player_elo + k_factor * (actual_outcome - expected_outcome)
        return new_elo

    def play_round(self, k_factor=32):
        for player in self.players:
            for opponent in self.players:
                if player != opponent:
                    player_score = self.get_score(player, opponent)
                    player_won = player_score > 0.5
                    player_elo = self.elo_rankings[player.getName()]
                    opponent_elo = self.elo_rankings[opponent.getName()]
                    new_player_elo = self.update_elo(player_elo, opponent_elo, player_won, k_factor)
                    new_opponent_elo = self.update_elo(opponent_elo, player_elo, not player_won, k_factor)
                    self.elo_rankings[player.getName()] = new_player_elo
                    self.elo_rankings[opponent.getName()] = new_opponent_elo

    def display_rankings(self):
        sorted_rankings = sorted(self.elo_rankings.items(), key=lambda x: x[1], reverse=True)
        for rank, (player_name, elo) in enumerate(sorted_rankings, start=1):
            print(f"{rank}. {player_name}: {round(elo)}")

    def play_and_display(self, num_matches=100):
        for i in range(num_matches):
            k_factor = 32 / (1 + i / 10)
            self.play_round(k_factor)
            print(f"Elo rankings after {i+1} matches:")
            self.display_rankings()
            print("\n")

    def get_score(self, player, opponent):
        env = ConnectFourEnv(opponent=opponent)
        obs, _ = env.reset()
        while True:
            action = player.play(obs)
            obs, rewards, dones, truncated, _ = env.step(action)
            if truncated or dones:
                obs, _ = env.reset()
                return rewards


if __name__ == "__main__":
    from connect_four_gymnasium.players import (
    AdultPlayer,
    AdultSmarterPlayer,
    BabyPlayer,
    ChildPlayer,
    ChildSmarterPlayer,
    TeenagerPlayer,
    TeenagerSmarterPlayer,
    MinMaxPlayer,
)
    # Create a list of players
    players = [
        BabyPlayer(),
        ChildPlayer(),
        ChildSmarterPlayer(),
        TeenagerPlayer(),
        TeenagerSmarterPlayer(),
        AdultPlayer(),
        AdultSmarterPlayer(),
        MinMaxPlayer(depth=1),
        MinMaxPlayer(depth=2),
        MinMaxPlayer(depth=3),
    ]

    elo_leaderboard = EloLeaderboard(players)
    elo_leaderboard.play_and_display()

# Elo rankings after 21 matches:
# 1.  AdultSmarterPlayer:    1767
# 2.  MinimaxPlayer depth 3: 1710
# 3.  AdultPlayer:           1689
# 4.  TeenagerSmarterPlayer: 1664
# 5.  TeenagerPlayer:        1644
# 6.  MinimaxPlayer depth 2: 1596
# 7.  ChildSmarterPlayer:    1548
# 8.  ChildPlayer:           1223
# 9.  MinimaxPlayer depth 1: 1174
# 10. BabyPlayer:             985