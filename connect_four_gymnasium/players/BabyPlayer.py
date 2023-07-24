import numpy as np
from .Player import Player

class BabyPlayer(Player):

    def __init__(self, _=""):
        pass

    def play(self, _):
        return np.random.randint(0, 7)
    def getName(self):
        return "BabyPlayer"
    def getElo(self):
        return 995
    def isDeterministic(self):
        return False