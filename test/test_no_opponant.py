import sys
import numpy as np
import pytest
sys.path.append('../')
from connect_four_gymnasium import ConnectFourEnv

from stable_baselines3 import PPO

def test_simple_moves_no_opponent():

    env = ConnectFourEnv(first_player=1)
    env.reset(seed=0)
    nextAction = 3
    board, rewards, dones, truncated, info = env.step(nextAction)
    
    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"
    
    expected_model_view = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, 0, 0, 0]
    ])
    
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

    nextAction = 0
    board, rewards, dones, truncated, info = env.step(nextAction)
    
    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"
    
    expected_model_view = np.array([
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 1, 0, 0, 0]
    ])
    
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

    nextAction = 3
    board, rewards, dones, truncated, info = env.step(nextAction)
    
    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"
    
    expected_model_view = np.array([
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0, -1, 0, 0, 0],
        [1, 0, 0, -1, 0, 0, 0]
    ])
    
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

    nextAction = 0
    board, rewards, dones, truncated, info = env.step(nextAction)
    
    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"
    
    expected_model_view = np.array([
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 1, 0, 0, 0],
        [-1, 0, 0, 1, 0, 0, 0]
    ])
    
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

    nextAction = 3
    board, rewards, dones, truncated, info = env.step(nextAction)
    
    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"
    
    expected_model_view = np.array([
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0, -1, 0, 0, 0],
        [1, 0, 0, -1, 0, 0, 0],
        [1, 0, 0, -1, 0, 0, 0]
    ])
    
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

    nextAction = 0
    board, rewards, dones, truncated, info = env.step(nextAction)
    
    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"
    
    expected_model_view = np.array([
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ -1, 0, 0, 1, 0, 0, 0],
        [ -1, 0, 0, 1, 0, 0, 0],
        [ -1, 0, 0, 1, 0, 0, 0]
    ])
    
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

    nextAction = 3
    board, rewards, dones, truncated, info = env.step(nextAction)
    
    assert rewards == 1, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == True, f"Expected dones: True but got {dones}"
    

if __name__ == "__main__":
    pytest.main()