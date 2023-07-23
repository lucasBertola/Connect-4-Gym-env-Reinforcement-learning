
import numpy as np
import copy


class BabyPlayer():
    def play(self, observation):
        return np.random.randint(0, 7)
    def getName(self):
        return "BabyPlayer"
    def isDeterministic(self):
        return False