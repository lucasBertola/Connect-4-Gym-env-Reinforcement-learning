import sys
import numpy as np
import pytest
sys.path.append('../')
from connect_four_gymnasium import ConnectFourEnv
from connect_four_gymnasium.players import BabyPlayer

from stable_baselines3 import PPO

def test_is_determinist_with_ppo():
    # Initialize the environment and the PPO model
    env = ConnectFourEnv(opponent=BabyPlayer())
    model = PPO("MlpPolicy", env, verbose=0, seed=0)

    # Train the model
    model.learn(total_timesteps=1000)

    # Test the model's determinism
    obs, _ = env.reset(seed=0)
    allrewards = []

    for i in range(1000):
        action, _states = model.predict(obs)
        obs, rewards, dones, truncated, info = env.step(action)

        if truncated or dones:
            allrewards.append(rewards)
            obs, _ = env.reset()

    # Check if the model is deterministic
    assert np.sum(allrewards) == 7, "The model is not determinist"


def test_is_working_with_ppo():
    # Initialize the environment and the PPO model
    env = ConnectFourEnv(opponent=BabyPlayer())
    model = PPO("MlpPolicy", env, verbose=0, seed=1)

    # Train the model
    model.learn(total_timesteps=10000)

    # Test the model's performance
    obs, _ = env.reset(seed=0)
    allrewards = []
    for i in range(1000):
        action, _states = model.predict(obs)
        obs, rewards, dones, truncated, info = env.step(action)

        if truncated or dones:
            allrewards.append(rewards)
            obs, _ = env.reset()

    # Check if the model finishes the game in less than 8 steps on average
    assert np.mean(allrewards) > 0.2, f"The model has not learned to play the game. Score {np.mean(allrewards)}"

def test_no_player_advantage():
    player1 = BabyPlayer()
    player2 = BabyPlayer()

    env = ConnectFourEnv(opponent=player2)
    obs, _ = env.reset(seed=0)
    allrewards = []
    for i in range(2000):
        action = player1.play(obs)
        obs, rewards, dones, truncated, info = env.step(action)

        if truncated or dones:
            allrewards.append(rewards)
            obs, _ = env.reset()
    assert np.mean(allrewards) < 0.05, f"The model is not equilibrated{np.mean(allrewards)}"
    assert np.mean(allrewards) > -0.05, f"The model is not equilibrated{np.mean(allrewards)}"

if __name__ == "__main__":
    pytest.main()