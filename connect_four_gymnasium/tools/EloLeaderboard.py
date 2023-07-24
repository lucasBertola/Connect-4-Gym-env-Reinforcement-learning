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
        self.players = [
            BabyPlayer(),
            ChildPlayer(),
            ChildSmarterPlayer(),
            TeenagerPlayer(),
            TeenagerSmarterPlayer(),
            AdultPlayer(),
            AdultSmarterPlayer()
        ]
        # Initialize the Elo rankings for each player
        self.elo_rankings = {player.getName(): player.getElo() if player.getElo() is not None else 1500 for player in self.players}

    def update_elo(self, player_elo, opponent_elo, player_won, k_factor=32):
        # Calculate the expected outcome based on the current Elo ratings
        expected_outcome = 1 / (1 + math.pow(10, (opponent_elo - player_elo) / 400))
        # Set the actual outcome based on whether the player won or lost
        actual_outcome = 1 if player_won else 0
        # Update the player's Elo rating
        new_elo = player_elo + k_factor * (actual_outcome - expected_outcome)
        return new_elo

    def play_round(self, k_factor=32, move_elo_already_known=False):
        # Iterate through all possible player-opponent pairs
        for player in self.players:
            for opponent in self.players:
                if player != opponent:
                    # Skip the match if both players have known Elo ratings and we don't want to update them
                    if not move_elo_already_known and player.getElo() is not None and opponent.getElo() is not None:
                        continue
                    player_score = self.get_score(player, opponent)
                    player_won = player_score > 0.5
                    player_elo = self.elo_rankings[player.getName()]
                    opponent_elo = self.elo_rankings[opponent.getName()]
                    new_player_elo = self.update_elo(player_elo, opponent_elo, player_won, k_factor)
                    new_opponent_elo = self.update_elo(opponent_elo, player_elo, not player_won, k_factor)
                    if player.getElo() is None or move_elo_already_known:
                        self.elo_rankings[player.getName()] = new_player_elo
                    if opponent.getElo() is None or move_elo_already_known:
                        self.elo_rankings[opponent.getName()] = new_opponent_elo

    def get_elo(self, new_players, num_matches=100, move_elo_already_known=False, display_log=True):
        # Add new players to the leaderboard
        self.players.extend(new_players)
        for player in new_players:
            self.elo_rankings[player.getName()] = player.getElo() if player.getElo() is not None else 1500

        # Play the specified number of matches
        for i in range(num_matches):
            k_factor = 32 / (1 + i / 10)
            self.play_round(k_factor, move_elo_already_known)
            if display_log:
                print(f"Elo rankings after {i+1} matches:")
                self.display_rankings()
                print("\n")

        # Return the updated Elo ratings for the new players
        new_player_elos = [self.elo_rankings[player.getName()] for player in new_players]
        return new_player_elos

    def display_rankings(self):
        # Sort the rankings in descending order of Elo ratings
        sorted_rankings = sorted(self.elo_rankings.items(), key=lambda x: x[1], reverse=True)
        # Display the sorted rankings
        for rank, (player_name, elo) in enumerate(sorted_rankings, start=1):
            print(f"{rank}. {player_name}: {round(elo)}")

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