import sys 
sys.path.append('../')
from connect_four_gymnasium import ConnectFourEnv
from connect_four_gymnasium.players import SelfTrained6Player
from connect_four_gymnasium.players import ConsolePlayer

from stable_baselines3 import PPO

you = ConsolePlayer()
env = ConnectFourEnv(opponent= SelfTrained6Player(deteministic=True), render_mode="human",main_player_name="you")

obs , _=  env.reset()
for i in range(5000):
    action = you.play(obs)
    obs, rewards, dones, truncated,info = env.step(action)
    env.render()
    if(truncated or dones):
        obs , _=  env.reset()