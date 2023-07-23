from .Player import Player

class ModelPlayer(Player):
    def __init__(self, model,name="Model",deteministic=True):
        self.model = model
        self.name = name
        self.deteministic = deteministic
    def play(self, observation):
        action, _states = self.model.predict(observation,deterministic=self.deteministic)
        return action
        
    def getName(self):
        return self.name
    
    def isDeterministic(self):
        return True