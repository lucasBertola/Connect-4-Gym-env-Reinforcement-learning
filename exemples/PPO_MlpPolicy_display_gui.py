import sys 
sys.path.append('../')
from connect_four_gymnasium import ConnectFourEnv
from connect_four_gymnasium.players import BabyPlayer

from stable_baselines3 import PPO
        
env = ConnectFourEnv(opponent=BabyPlayer())
model = PPO("MlpPolicy", env, verbose=1)

model.learn(total_timesteps=(50000))

env = ConnectFourEnv(opponent= BabyPlayer(), render_mode="human")

obs , _=  env.reset()
for i in range(5000):
    action, _states = model.predict(obs,deterministic=True)
    obs, rewards, dones, truncated,info = env.step(action)
    env.render()
    if(truncated or dones):
        obs , _=  env.reset()