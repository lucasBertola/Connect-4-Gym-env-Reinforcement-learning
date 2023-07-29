from .Player import Player

class ModelPlayer(Player):
    def __init__(self, model,name="Model",deteministic=True):
        self.model = model
        self.name = name
        self.deteministic = deteministic
    def play(self, observations): #todo other bot : make able to takes multiples observations
        actions, _states = self.model.predict(observations,deterministic=self.deteministic)
        return actions
        
    def getName(self):
        return self.name
    
    def isDeterministic(self):
        return self.deteministic
    
    def getElo(self):
        return None