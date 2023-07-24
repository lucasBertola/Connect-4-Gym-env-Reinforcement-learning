import numpy as np
from .Player import Player

class ChildPlayer(Player):

    def __init__(self, _=""):
        pass
    def play(self, observation):
        # Check if a winning move is available for the player
        for move in range(7):
            if observation[0, move] == 0:
                new_board = self.apply_move(observation, move, 1)
                if self.check_win(new_board, 1):
                    return move

        return np.random.choice(range(7))

    def getName(self):
        return "ChildPlayer"
    
    def getElo(self):
        return 1208
    
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