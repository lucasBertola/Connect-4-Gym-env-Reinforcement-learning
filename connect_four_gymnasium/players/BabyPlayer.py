import numpy as np
from .Player import Player

class BabyPlayer(Player):

    def __init__(self, _=""):
        pass

    def random_move(self):
        return np.random.randint(0, 7)

    def play(self, obs):
        if isinstance(obs, list):
            return [self.random_move() for _ in range(len(obs))]
        else:
            return self.random_move()

    def getName(self):
        return "BabyPlayer"

    def getElo(self):
        return 1000

    def isDeterministic(self):
        return False