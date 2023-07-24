class Player:
    def __init__(self, name):
        self.name = name

    def play(self, observation):
        raise NotImplementedError("The 'play' method must be implemented in the child class")

    def getElo(self):
        return None
    
    def getName(self):
        return self.name

    def isDeterministic(self):
        raise NotImplementedError("The 'isDeterministic' method must be implemented in the child class")