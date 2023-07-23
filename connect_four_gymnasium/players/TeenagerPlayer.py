import numpy as np
from .Player import Player


class TeenagerPlayer(Player):

    def __init__(self, _=""):
        pass
    
    def play(self, observation):
        moves_to_avoid = []

        # Check for a winning move for the player
        for move in range(7):
            if observation[0, move] == 0:
                new_board = self.apply_move(observation, move, 1)
                if self.check_win(new_board, 1):
                    return move

        # Check for a winning move for the opponent
        for move in range(7):
            if observation[0, move] == 0:
                new_board = self.apply_move(observation, move, 2)
                if self.check_win(new_board, 2):
                    return move

        # Check if a move allows the opponent to win by playing the same move again
        for move in range(7):
            if observation[0, move] == 0:
                new_board = self.apply_move(observation, move, 1)
                new_board = self.apply_move(new_board, move, 2)
                if self.check_win(new_board, 2):
                    moves_to_avoid.append(move)

        # Play a random move among valid moves, excluding moves_to_avoid
        valid_moves = [c for c in range(7) if observation[0, c] == 0 and c not in moves_to_avoid]

        # If valid_moves is empty, choose a random move among all possible moves
        if not valid_moves:
            valid_moves = [c for c in range(7) if observation[0, c] == 0]

        return np.random.choice(valid_moves)

    def getName(self):
        return "TeenagerPlayer"

    def isDeterministic(self):
        return False

    def apply_move(self, board, move, player):
        new_board = board.copy()
        for i in range(5, -1, -1):
            if new_board[i, move] == 0:
                new_board[i, move] = player
                break
        return new_board

    def check_win(self, board, player):
        for i in range(6):
            for j in range(4):
                if (board[i, j:j+4] == player).all():
                    return True
        for i in range(3):
            for j in range(7):
                if (board[i:i+4, j] == player).all():
                    return True
        for i in range(3):
            for j in range(4):
                if (board[i:i+4, j:j+4].diagonal() == player).all():
                    return True
                if (board[i:i+4, j:j+4][::-1].diagonal() == player).all():
                    return True
        return False