import numpy as np
from .Player import Player


class TeenagerPlayer(Player):

    def __init__(self, _=""):
        pass

    def play_single(self, observation):
        moves_to_avoid = []

        # Check for a winning move for the player
        for move in range(7):
            if observation[0, move] == 0:
                new_board, row, col = self.apply_move(observation, move, 1)
                if self.check_win_around_last_move(new_board, 1, row, col):
                    return move

        # Check for a winning move for the opponent
        for move in range(7):
            if observation[0, move] == 0:
                new_board, row, col = self.apply_move(observation, move, -1)
                if self.check_win_around_last_move(new_board, -1, row, col):
                    return move

        # Check if a move allows the opponent to win by playing the same move again
        for move in range(7):
            if observation[0, move] == 0:
                new_board, row, col = self.apply_move(observation, move, 1)
                if new_board[0, move] == 0:
                    new_board, row, col = self.apply_move(new_board, move, -1)
                    if self.check_win_around_last_move(new_board, -1, row, col):
                        moves_to_avoid.append(move)

        # Play a random move among valid moves, excluding moves_to_avoid
        valid_moves = [c for c in range(7) if observation[0, c] == 0 and c not in moves_to_avoid]

        # If valid_moves is empty, choose a random move among all possible moves
        if not valid_moves:
            valid_moves = [c for c in range(7) if observation[0, c] == 0]

        if not valid_moves:
            print('no valid_move.. i don t want to suicide myself',valid_moves,observation)
            exit()

        return np.random.choice(valid_moves)

    def play(self, obs):
        if isinstance(obs, list):
            return [self.play_single(o) for o in obs]
        else:
            return self.play_single(obs)

    def getName(self):
        return "TeenagerPlayer"

    def getElo(self):
        return 1657

    def isDeterministic(self):
        return False

    def apply_move(self, board, move, player):
        new_board = board.copy()
        for i in range(5, -1, -1):
            if new_board[i, move] == 0:
                new_board[i, move] = player
                return new_board, i, move
        print('wtf')
        exit()

    def check_win_around_last_move(self, board, player, row, col):
        directions = [
            (1, 0),  # horizontal
            (0, 1),  # vertical
            (1, 1),  # diagonal /
            (1, -1)  # diagonal \
        ]

        for dr, dc in directions:
            count = 0
            for step in range(-3, 4):
                r, c = row + step * dr, col + step * dc
                if 0 <= r < 6 and 0 <= c < 7 and board[r, c] == player:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0

        return False