import numpy as np
from .Player import Player

class BabySmarterPlayer(Player):

    def __init__(self, _=""):
        pass

    def play_single(self,obs):
        valid_moves = [c for c in range(7) if obs[0, c] == 0]
        return np.random.choice(valid_moves)

    def play(self, obs):
        if isinstance(obs, list):
            return [self.play_single(obs) for _ in range(len(obs))]
        else:
            return self.play_single(obs)

    def getName(self):
        return "BabySmarterPlayer"

    def getElo(self):
        return 1060

    def isDeterministic(self):
        return False
    

    # Play a random move
        valid_moves = [c for c in range(7) if observation[0, c] == 0]
        return np.random.choice(valid_moves)