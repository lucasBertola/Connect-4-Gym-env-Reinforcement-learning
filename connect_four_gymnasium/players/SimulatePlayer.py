from .Player import Player
import copy
class SimulatePlayer(Player):

    def __init__(self, _=""):
        self.nextMove = 0
        self.lastBoardView = None
        pass
    
    def set_next_move(self, move):
        self.nextMove = move
        assert self.nextMove >= 0 and self.nextMove <= 6 
    def play(self, board):
        self.lastBoardView = copy.deepcopy(board)
        return self.nextMove
    def getName(self):
        return "SimulatePlayer"
    def getElo(self):
        return None
    def isDeterministic(self):
        return False