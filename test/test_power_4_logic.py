import sys
import numpy as np
import pytest
sys.path.append('../')
from connect_four_gymnasium import ConnectFourEnv
from connect_four_gymnasium.players import SimulatePlayer

from stable_baselines3 import PPO

def test_place_a_simple_move():
    simulatePlayer = SimulatePlayer()


    env = ConnectFourEnv(opponent=simulatePlayer,first_player=1)
    env.reset(seed=0)
    nextAction = 3
    simulatePlayer.set_next_move(0)
    board, rewards, dones, truncated, info = env.step(nextAction)
    
    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"
    
    expected_opponant_view = np.array([
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0, -1, 0, 0, 0]
    ])
    
    expected_model_view = np.array([
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 1, 0, 0, 0]
    ])
    
    assert np.array_equal(simulatePlayer.lastBoardView, expected_opponant_view), f"expected_opponant_view:\n{expected_opponant_view}\nbut got:\n{simulatePlayer.lastBoardView}"
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"


def test_place_a_simple_game_horizontal_win():
    simulatePlayer = SimulatePlayer()


    env = ConnectFourEnv(opponent=simulatePlayer,first_player=1)
    env.reset(seed=0)
    nextAction = 0
    simulatePlayer.set_next_move(0)
    board, rewards, dones, truncated, info = env.step(nextAction)
    
    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"
    
    expected_opponant_view = np.array([
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0]
    ])
    
    expected_model_view = np.array([
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0],
        [ 1, 0, 0, 0, 0, 0, 0]
    ])
    
    assert np.array_equal(simulatePlayer.lastBoardView, expected_opponant_view), f"expected_opponant_view:\n{expected_opponant_view}\nbut got:\n{simulatePlayer.lastBoardView}"
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

    nextAction = 1
    simulatePlayer.set_next_move(1)
    board, rewards, dones, truncated, info = env.step(nextAction)
    
    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"
    
    expected_opponant_view = np.array([
        [ 0,  0, 0, 0, 0, 0, 0],
        [ 0,  0, 0, 0, 0, 0, 0],
        [ 0,  0, 0, 0, 0, 0, 0],
        [ 0,  0, 0, 0, 0, 0, 0],
        [ 1,  0, 0, 0, 0, 0, 0],
        [-1, -1, 0, 0, 0, 0, 0]
    ])
    
    expected_model_view = np.array([
        [ 0,  0, 0, 0, 0, 0, 0],
        [ 0,  0, 0, 0, 0, 0, 0],
        [ 0,  0, 0, 0, 0, 0, 0],
        [ 0,  0, 0, 0, 0, 0, 0],
        [-1, -1, 0, 0, 0, 0, 0],
        [ 1,  1, 0, 0, 0, 0, 0]
    ])
    
    assert np.array_equal(simulatePlayer.lastBoardView, expected_opponant_view), f"expected_opponant_view:\n{expected_opponant_view}\nbut got:\n{simulatePlayer.lastBoardView}"
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

    nextAction = 2
    simulatePlayer.set_next_move(1)
    board, rewards, dones, truncated, info = env.step(nextAction)
    
    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"
    
    expected_opponant_view = np.array([
        [ 0,  0,  0, 0, 0, 0, 0],
        [ 0,  0,  0, 0, 0, 0, 0],
        [ 0,  0,  0, 0, 0, 0, 0],
        [ 0,  0,  0, 0, 0, 0, 0],
        [ 1,  1,  0, 0, 0, 0, 0],
        [-1, -1, -1, 0, 0, 0, 0]
    ])
    
    expected_model_view = np.array([
        [ 0,  0, 0, 0, 0, 0, 0],
        [ 0,  0, 0, 0, 0, 0, 0],
        [ 0,  0, 0, 0, 0, 0, 0],
        [ 0, -1, 0, 0, 0, 0, 0],
        [-1, -1, 0, 0, 0, 0, 0],
        [ 1,  1, 1, 0, 0, 0, 0]
    ])
    
    assert np.array_equal(simulatePlayer.lastBoardView, expected_opponant_view), f"expected_opponant_view:\n{expected_opponant_view}\nbut got:\n{simulatePlayer.lastBoardView}"
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

    nextAction = 3
    simulatePlayer.set_next_move(1)
    board, rewards, dones, truncated, info = env.step(nextAction)
    
    assert rewards == 1, f"Expected reward: 1 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == True, f"Expected dones: True but got {dones}"
    
    expected_opponant_view = np.array([ # he doesn't view your move because you win before
        [ 0,  0,  0, 0, 0, 0, 0],
        [ 0,  0,  0, 0, 0, 0, 0],
        [ 0,  0,  0, 0, 0, 0, 0],
        [ 0,  0,  0, 0, 0, 0, 0],
        [ 1,  1,  0, 0, 0, 0, 0],
        [-1, -1, -1, 0, 0, 0, 0]
    ])
    
    expected_model_view = np.array([
        [ 0,  0, 0, 0, 0, 0, 0],
        [ 0,  0, 0, 0, 0, 0, 0],
        [ 0,  0, 0, 0, 0, 0, 0],
        [ 0,  1, 0, 0, 0, 0, 0],
        [ 1,  1, 0, 0, 0, 0, 0],
        [-1, -1,-1,-1, 0, 0, 0]
    ])
    
    assert np.array_equal(simulatePlayer.lastBoardView, expected_opponant_view), f"expected_opponant_view:\n{expected_opponant_view}\nbut got:\n{simulatePlayer.lastBoardView}"
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

def test_place_a_simple_game_vertical_win():
    simulatePlayer = SimulatePlayer()

    env = ConnectFourEnv(opponent=simulatePlayer,first_player=1)
    env.reset(seed=0)
    nextAction = 1
    simulatePlayer.set_next_move(3)
    board, rewards, dones, truncated, info = env.step(nextAction)
    
    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"
    
    expected_opponant_view = np.array([
        [0,  0, 0, 0, 0, 0, 0],
        [0,  0, 0, 0, 0, 0, 0],
        [0,  0, 0, 0, 0, 0, 0],
        [0,  0, 0, 0, 0, 0, 0],
        [0,  0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0]
    ])
    
    expected_model_view = np.array([
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0,  0, 0, 0, 0],
        [0, 1, 0, -1, 0, 0, 0]
    ])
    
    assert np.array_equal(simulatePlayer.lastBoardView, expected_opponant_view), f"expected_opponant_view:\n{expected_opponant_view}\nbut got:\n{simulatePlayer.lastBoardView}"
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

    nextAction = 1
    simulatePlayer.set_next_move(6)
    board, rewards, dones, truncated, info = env.step(nextAction)

    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"
    
    expected_opponant_view = np.array([
        [0,  0, 0, 0, 0, 0, 0],
        [0,  0, 0, 0, 0, 0, 0],
        [0,  0, 0, 0, 0, 0, 0],
        [0,  0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0],
        [0, -1, 0, 1, 0, 0, 0]
    ])
    
    expected_model_view = np.array([
        [0, 0, 0,  0, 0, 0,  0],
        [0, 0, 0,  0, 0, 0,  0],
        [0, 0, 0,  0, 0, 0,  0],
        [0, 0, 0,  0, 0, 0,  0],
        [0, 1, 0,  0, 0, 0,  0],
        [0, 1, 0, -1, 0, 0, -1]
    ])
    
    assert np.array_equal(simulatePlayer.lastBoardView, expected_opponant_view), f"expected_opponant_view:\n{expected_opponant_view}\nbut got:\n{simulatePlayer.lastBoardView}"
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

    nextAction = 1
    simulatePlayer.set_next_move(5)
    board, rewards, dones, truncated, info = env.step(nextAction)

    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"
    
    expected_opponant_view = np.array([
        [0,  0, 0, 0, 0, 0, 0],
        [0,  0, 0, 0, 0, 0, 0],
        [0,  0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0],
        [0, -1, 0, 1, 0, 0, 1]
    ])
    
    expected_model_view = np.array([
        [0, 0, 0,  0, 0,  0,  0],
        [0, 0, 0,  0, 0,  0,  0],
        [0, 0, 0,  0, 0,  0,  0],
        [0, 1, 0,  0, 0,  0,  0],
        [0, 1, 0,  0, 0,  0,  0],
        [0, 1, 0, -1, 0, -1, -1]
    ])
    
    assert np.array_equal(simulatePlayer.lastBoardView, expected_opponant_view), f"expected_opponant_view:\n{expected_opponant_view}\nbut got:\n{simulatePlayer.lastBoardView}"
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

    nextAction = 1
    simulatePlayer.set_next_move(4)
    board, rewards, dones, truncated, info = env.step(nextAction)

    assert rewards == 1, f"Expected reward: 1 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == True, f"Expected dones: True but got {dones}"
        
    expected_model_view = np.array([
        [0,  0, 0, 0, 0, 0, 0],
        [0,  0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0],
        [0, -1, 0, 1, 0, 1, 1]
    ])
    
    assert np.array_equal(simulatePlayer.lastBoardView, expected_opponant_view), f"expected_opponant_view:\n{expected_opponant_view}\nbut got:\n{simulatePlayer.lastBoardView}"
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"


def test_place_a_simple_game_updiagonal_win():
    simulatePlayer = SimulatePlayer()

    env = ConnectFourEnv(opponent=simulatePlayer,first_player=1)
    env.reset(seed=0)
    nextAction = 0
    simulatePlayer.set_next_move(1)
    board, rewards, dones, truncated, info = env.step(nextAction)
    
    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"
    
    expected_opponant_view = np.array([
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0]
    ])
    
    expected_model_view = np.array([
        [0,  0, 0, 0, 0, 0, 0],
        [0,  0, 0, 0, 0, 0, 0],
        [0,  0, 0, 0, 0, 0, 0],
        [0,  0, 0, 0, 0, 0, 0],
        [0,  0, 0, 0, 0, 0, 0],
        [1, -1, 0, 0, 0, 0, 0]
    ])
    
    assert np.array_equal(simulatePlayer.lastBoardView, expected_opponant_view), f"expected_opponant_view:\n{expected_opponant_view}\nbut got:\n{simulatePlayer.lastBoardView}"
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

    nextAction = 1
    simulatePlayer.set_next_move(2)
    board, rewards, dones, truncated, info = env.step(nextAction)

    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"
    
    expected_opponant_view = np.array([
        [ 0,  0, 0, 0, 0, 0, 0],
        [ 0,  0, 0, 0, 0, 0, 0],
        [ 0,  0, 0, 0, 0, 0, 0],
        [ 0,  0, 0, 0, 0, 0, 0],
        [ 0, -1, 0, 0, 0, 0, 0],
        [-1,  1, 0, 0, 0, 0, 0]
    ])
    
    expected_model_view = np.array([
        [0,  0,  0, 0, 0, 0, 0],
        [0,  0,  0, 0, 0, 0, 0],
        [0,  0,  0, 0, 0, 0, 0],
        [0,  0,  0, 0, 0, 0, 0],
        [0,  1,  0, 0, 0, 0, 0],
        [1, -1, -1, 0, 0, 0, 0]
    ])
    
    assert np.array_equal(simulatePlayer.lastBoardView, expected_opponant_view), f"expected_opponant_view:\n{expected_opponant_view}\nbut got:\n{simulatePlayer.lastBoardView}"
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

    nextAction = 3
    simulatePlayer.set_next_move(2)
    board, rewards, dones, truncated, info = env.step(nextAction)

    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"
    
    expected_opponant_view = np.array([
        [ 0,  0, 0,  0, 0, 0, 0],
        [ 0,  0, 0,  0, 0, 0, 0],
        [ 0,  0, 0,  0, 0, 0, 0],
        [ 0,  0, 0,  0, 0, 0, 0],
        [ 0, -1, 0,  0, 0, 0, 0],
        [-1,  1, 1, -1, 0, 0, 0]
    ])
    
    expected_model_view = np.array([
        [0,  0,  0, 0, 0, 0, 0],
        [0,  0,  0, 0, 0, 0, 0],
        [0,  0,  0, 0, 0, 0, 0],
        [0,  0,  0, 0, 0, 0, 0],
        [0,  1, -1, 0, 0, 0, 0],
        [1, -1, -1, 1, 0, 0, 0]
    ])
    
    assert np.array_equal(simulatePlayer.lastBoardView, expected_opponant_view), f"expected_opponant_view:\n{expected_opponant_view}\nbut got:\n{simulatePlayer.lastBoardView}"
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

    nextAction = 2
    simulatePlayer.set_next_move(3)
    board, rewards, dones, truncated, info = env.step(nextAction)

    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"
    
    expected_opponant_view = np.array([
        [ 0,  0,  0,  0, 0, 0, 0],
        [ 0,  0,  0,  0, 0, 0, 0],
        [ 0,  0,  0,  0, 0, 0, 0],
        [ 0,  0, -1,  0, 0, 0, 0],
        [ 0, -1,  1,  0, 0, 0, 0],
        [-1,  1,  1, -1, 0, 0, 0]
    ])
    
    expected_model_view = np.array([
        [0,  0,  0,  0, 0, 0, 0],
        [0,  0,  0,  0, 0, 0, 0],
        [0,  0,  0,  0, 0, 0, 0],
        [0,  0,  1,  0, 0, 0, 0],
        [0,  1, -1, -1, 0, 0, 0],
        [1, -1, -1,  1, 0, 0, 0]
    ])
    
    assert np.array_equal(simulatePlayer.lastBoardView, expected_opponant_view), f"expected_opponant_view:\n{expected_opponant_view}\nbut got:\n{simulatePlayer.lastBoardView}"
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"  

    nextAction = 2
    simulatePlayer.set_next_move(3)
    board, rewards, dones, truncated, info = env.step(nextAction)

    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"
    
    expected_opponant_view = np.array([
        [ 0,  0,  0,  0, 0, 0, 0],
        [ 0,  0,  0,  0, 0, 0, 0],
        [ 0,  0, -1,  0, 0, 0, 0],
        [ 0,  0, -1,  0, 0, 0, 0],
        [ 0, -1,  1,  1, 0, 0, 0],
        [-1,  1,  1, -1, 0, 0, 0]
    ])
    
    expected_model_view = np.array([
        [0,  0,  0,  0, 0, 0, 0],
        [0,  0,  0,  0, 0, 0, 0],
        [0,  0,  1,  0, 0, 0, 0],
        [0,  0,  1, -1, 0, 0, 0],
        [0,  1, -1, -1, 0, 0, 0],
        [1, -1, -1,  1, 0, 0, 0]
    ])
    
    assert np.array_equal(simulatePlayer.lastBoardView, expected_opponant_view), f"expected_opponant_view:\n{expected_opponant_view}\nbut got:\n{simulatePlayer.lastBoardView}"
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"   

    nextAction = 3
    simulatePlayer.set_next_move(3)
    board, rewards, dones, truncated, info = env.step(nextAction)

    assert rewards == 1, f"Expected reward: 1 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == True, f"Expected dones: True but got {dones}"
    
    expected_model_view = np.array([
        [ 0,  0,  0,  0, 0, 0, 0],
        [ 0,  0,  0,  0, 0, 0, 0],
        [ 0,  0, -1, -1, 0, 0, 0],
        [ 0,  0, -1,  1, 0, 0, 0],
        [ 0, -1,  1,  1, 0, 0, 0],
        [-1,  1,  1, -1, 0, 0, 0]
    ])
    
    assert np.array_equal(simulatePlayer.lastBoardView, expected_opponant_view), f"expected_opponant_view:\n{expected_opponant_view}\nbut got:\n{simulatePlayer.lastBoardView}"
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"   

def test_place_a_simple_game_downdiagonal_win():
    simulatePlayer = SimulatePlayer()

    env = ConnectFourEnv(opponent=simulatePlayer, first_player=1)
    env.reset(seed=0)
    nextAction = 5
    simulatePlayer.set_next_move(4)
    board, rewards, dones, truncated, info = env.step(nextAction)

    nextAction = 4
    simulatePlayer.set_next_move(3)
    board, rewards, dones, truncated, info = env.step(nextAction)

    nextAction = 2
    simulatePlayer.set_next_move(3)
    board, rewards, dones, truncated, info = env.step(nextAction)

    nextAction = 3
    simulatePlayer.set_next_move(2)
    board, rewards, dones, truncated, info = env.step(nextAction)

    nextAction = 2
    simulatePlayer.set_next_move(1)
    board, rewards, dones, truncated, info = env.step(nextAction)

    nextAction = 2
    board, rewards, dones, truncated, info = env.step(nextAction)

    expected_model_view = np.array([
        [0,  0,  0,  0,  0,  0, 0],
        [0,  0,  0,  0,  0,  0, 0],
        [0,  0, -1,  0,  0,  0, 0],
        [0,  0, -1, -1,  0,  0, 0],
        [0,  0,  1,  1, -1,  0, 0],
        [0,  1, -1,  1,  1, -1, 0]
    ])

    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

    assert rewards == 1, f"Expected reward: 1 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == True, f"Expected dones: True but got {dones}"

def test_second_player_can_begin():
    simulatePlayer = SimulatePlayer()


    env = ConnectFourEnv(opponent=simulatePlayer,first_player=-1)
    simulatePlayer.set_next_move(0)
    board, _ = env.reset(seed=0)
    
    expected_opponant_view = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ])

    expected_model_view = np.array([
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0]
    ])

    assert np.array_equal(simulatePlayer.lastBoardView, expected_opponant_view), f"expected_opponant_view:\n{expected_opponant_view}\nbut got:\n{simulatePlayer.lastBoardView}"
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

    nextAction = 3
    simulatePlayer.set_next_move(4)
    board, rewards, dones, truncated, info = env.step(nextAction)
    
    assert rewards == 0, f"Expected reward: 0 but got {rewards}"
    assert truncated == False, f"Expected truncated: False but got {truncated}"
    assert dones == False, f"Expected dones: False but got {dones}"

    expected_opponant_view = np.array([
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0,  0, 0, 0, 0],
        [0, 0, 0,  0, 0, 0, 0],
        [1, 0, 0, -1, 0, 0, 0]
    ])

    expected_model_view = np.array([
        [ 0, 0, 0, 0,  0, 0, 0],
        [ 0, 0, 0, 0,  0, 0, 0],
        [ 0, 0, 0, 0,  0, 0, 0],
        [ 0, 0, 0, 0,  0, 0, 0],
        [ 0, 0, 0, 0,  0, 0, 0],
        [-1, 0, 0, 1, -1, 0, 0]
    ])

    
    
    assert np.array_equal(simulatePlayer.lastBoardView, expected_opponant_view), f"expected_opponant_view:\n{expected_opponant_view}\nbut got:\n{simulatePlayer.lastBoardView}"
    assert np.array_equal(board, expected_model_view), f"Expected board:\n{expected_model_view}\nbut got:\n{board}"

if __name__ == "__main__":
    pytest.main()