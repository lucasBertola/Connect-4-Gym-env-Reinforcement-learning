from .Player import Player
import torch.nn as nn
import torch.nn.functional as F
import torch
import numpy as np



NUM_BLOCKS = 8
NUM_CHANNELS = 128
LEARNING_RATE = 0.001
MCTS_ITERATIONS = 100
C_PUCT = 2.0
DIRICHLET_EPSILON = 0.1
DIRICHLET_ALPHA = 1.4

class ResBlock(nn.Module):
  def __init__(self, num_channels):
    super(ResBlock, self).__init__()
    self.conv_1 = nn.Conv2d(num_channels, num_channels, kernel_size=3, padding=1)
    self.bn_1 = nn.BatchNorm2d(num_channels)
    self.conv_2 = nn.Conv2d(num_channels, num_channels, kernel_size=3, padding=1)
    self.bn_2 = nn.BatchNorm2d(num_channels)

  def forward(self, x):
    r = x
    x = self.conv_1(x)
    x = self.bn_1(x)
    x = F.relu(x)
    x = self.conv_2(x)
    x = self.bn_2(x)
    x += r
    x = F.relu(x)
    return x

class ResNet(nn.Module):
  def __init__(self, num_blocks, num_channels):
    super(ResNet, self).__init__()
    state_size = 42 #7*6
    action_size = 7 #7*6
    self.start_block = nn.Sequential(
      nn.Conv2d(2, num_channels, kernel_size=3, padding=1), 
      nn.BatchNorm2d(num_channels),
      nn.ReLU()
    )
    self.res_blocks = nn.ModuleList([ResBlock(num_channels) for i in range(num_blocks)])
    self.policy_head = nn.Sequential(
      nn.Conv2d(num_channels, 32, kernel_size=3, padding=1),
      nn.BatchNorm2d(32),
      nn.ReLU(),
      nn.Flatten(),
      nn.Linear(32 * state_size, action_size)
    )
    self.value_head = nn.Sequential(
      nn.Conv2d(num_channels, 3, kernel_size=3, padding=1), 
      nn.BatchNorm2d(3),
      nn.ReLU(),
      nn.Flatten(),
      nn.Linear(3 * state_size, 1),
      nn.Tanh()
    )

  def forward(self, x):
    x = self.start_block(x)
    for res_block in self.res_blocks:
      x = res_block(x)
    policy = self.policy_head(x)
    value = self.value_head(x)
    return policy, 0

class AlphaFour:
  def __init__(self):
    self.model = ResNet(NUM_BLOCKS, NUM_CHANNELS)
    import os
    current_script_path = os.path.dirname(os.path.realpath(__file__))
    weights_file_path =current_script_path+'/SelfTrained6PlayerWeight.pt'
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    self.model.load_state_dict(torch.load(weights_file_path, map_location=device))

  def obs_to_tensor(self, states):
    states = np.stack(states)
    encoded_states = np.stack((states == 1, states == -1)).swapaxes(0, 1)
    return torch.tensor(encoded_states, dtype=torch.float32)





class SelfTrained6Player(Player):
    def __init__(self, name="SelfTrained6Player",deteministic=False):
        self.alphaFour = AlphaFour()
        self.alphaFour.model.eval()
        self.name = name
        self.deteministic = deteministic

    def play(self, observations):
        hasToReturnList = True
        if not isinstance(observations, list):
            observations = [observations]
            hasToReturnList = False

        with torch.no_grad():
          pred_policies, pred_values = self.alphaFour.model(self.alphaFour.obs_to_tensor(observations))

        actions = []
        for policy in pred_policies:
            if self.deteministic:
                actions.append(np.argmax(policy))
            else:
                action_choices = np.arange(len(policy))
                probabilities = torch.softmax(policy, dim=0).numpy()
                chosen_action = np.random.choice(action_choices, p=probabilities)
                actions.append(chosen_action)

        if hasToReturnList:
           return np.array(actions)
        else:
           return actions[0]
        
        
        
    def getName(self):
        return self.name
    
    def isDeterministic(self):
        return self.deteministic
    
    def getElo(self):
       return 2410
    