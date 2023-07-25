<p align="center">
    <img src="https://github.com/lucasBertola/Connect-4-Gym-env-Reinforcement-learning/blob/main/ressources/gifRobot.gif" width="500px"/>
</p>

# Connect Four Environment

Welcome to the Connect 4 Environment repository! This environment is specifically designed for training reinforcement learning models to learn how to play the classic Connect Four game on their own, without any human intervention. The environment is compatible with the OpenAI Gym / Gymnasium interface, making it easy to integrate with a wide range of reinforcement learning libraries and algorithms.

The main goal of this project is to provide a simple and easy-to-use environment for training AI models, allowing you to focus on developing and improving your AI algorithms without spending time on creating an environment from scratch.

## Features

- **OpenAI Gym / Gymnasium Compatible**: Connect Four follows the OpenAI Gym / Gymnasium interface, making it compatible with a wide range of reinforcement learning libraries and algorithms.
- **Variety of Bots**: The environment includes a collection of Connect Four bots with different skill levels to help with the learning process and provide a diverse range of opponents.
- **Elo Leaderboard System**: Evaluate the performance of your AI model by assigning an Elo rating using the provided leaderboard system. This allows you to track your bot's progress and compare it to other bots.
- **Play Against Your AI**: Test your own skills against your AI model by playing against it in a console-based interface. This is a great way to see how well your AI has learned and to have some fun while doing it!
- **FCN and CNN Compatible**: The environment is designed to work seamlessly with both FCN and CNN policies. This makes it a great playground to experiment with different types of neural networks.
- **Human Render Mode**: Watch your agent learn in real-time with the human render mode. It's not just about the numbers, it's also about the journey!
- **Two-Player Mode**: Train your agent against another AI or even a human opponent to test its performance in real-world scenarios.
- **Self-Play Training**: The environment supports self-play training, allowing your AI model to learn by playing against itself, similar to the approach used by AlphaGo Zero. This can lead to more advanced strategies and a deeper understanding of the game as the model continuously improves through self-play.
- **Optimized Performance**: The environment has been specifically designed with performance in mind, ensuring that your models spend their time learning rather than playing the game. This allows for faster training and more efficient use of computational resources.


## Installation

To use the MiniGrid environment, you can install it directly into your project using pip:

```bash
pip install gymnasium-connect-four
```

## Usage

Import the `ConnectFourEnv` class, and his opponant (for exemple the very easy player `BabyPlayer` )

```python
from connect_four_gymnasium import ConnectFourEnv
from connect_four_gymnasium.players import BabyPlayer
```

Here is a simple example of how to use the environment with PPO:

```python
from connect_four_gymnasium import ConnectFourEnv
from connect_four_gymnasium.players import BabyPlayer
from stable_baselines3 import PPO
        
env = ConnectFourEnv(opponent=BabyPlayer())
model = PPO("MlpPolicy", env, verbose=1)

model.learn(total_timesteps=(100000))
```

For detailed usage instructions and examples, please refer to the [examples](https://github.com/lucasBertola/Connect-4-Gym-env-Reinforcement-learning/tree/main/exemples) directory or check out our [Colab Notebook](https://colab.research.google.com/github/lucasBertola/Connect-4-Gym-env-Reinforcement-learning/blob/main/exemples/PPO_MlpPolicy.ipynb).

<a href="https://colab.research.google.com/github/lucasBertola/Connect-4-env/blob/main/exemples/PPO_MlpPolicy.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>

## Environment Details

In this section, we provide an overview of the Connect Four environment, including the action space, observation space, rewards, and episode termination conditions.

### Action Space

The action space in the Connect Four environment is discrete, with a total of 7 possible actions. Each action corresponds to a column in the game board where a player can drop their piece. The action space is represented as follows:

```python
self.action_space = spaces.Discrete(self.COLUMNS_COUNT)
```

### Observation Space

The observation space in the Connect Four environment is a 2D array representing the game board. Each cell in the array can have one of three possible values: 0 (empty), 1 (player's piece), or 2 (opponent's piece). The observation space is defined as follows:

```python
self.observation_space = spaces.Box(low=0, high=2, shape=(self.ROWS_COUNT, self.COLUMNS_COUNT), dtype=np.int32)
```

### Rewards

The reward system in the Connect Four environment is designed to encourage the AI model to learn how to win the game. The rewards are as follows:

- A reward of +1 is given when the AI model wins the game by connecting four of its pieces in a row, either horizontally, vertically, or diagonally.
- A reward of -1 is given when the AI model loses the game or plays an invalid action.
- A reward of 0 is given for all other actions that do not result in a win or loss.

### Episode Termination

An episode in the Connect Four environment terminates under the following conditions:

- The AI model wins the game by connecting four of its pieces in a row, either horizontally, vertically, or diagonally.
- The AI model loses the game by allowing the opponent to connect four of their pieces in a row, or by playing an invalid action.
- The game board is completely filled, resulting in a draw.

When an episode terminates, the environment is reset, and a new episode begins.

## Available Players

This library provides a collection of Connect Four bots with different skill levels. These bots can be used for various purposes, such as:

- **Learning by playing against them**: You can improve your AI model by playing against these bots, which range from beginner to advanced levels.
- **Comparing the level of self-learning models**: By playing against these bots, you can evaluate the performance of your self-learning model and position it in terms of skill level and elo.

You can integrate players as opponents in your gym environment like this:

```python
env = ConnectFourEnv(opponent=BabyPlayer())
```

### Player Descriptions

- **MinMaxPlayer**: An implementation of the Minimax algorithm. Can be used with different search depths (e.g., `MinMaxPlayer(depth=3)`), but it is very slow, so it is not recommended for general use. All other algorithms are much faster.

- **BabyPlayer**: Plays random moves.

- **ChildPlayer**: Plays random moves, but if there is a winning move, it will play it.

- **ChildSmarterPlayer**: Same as ChildPlayer, but if there is a move that would make the opponent win, it will play that move to block the opponent.

- **TeenagerPlayer**: Same as ChildSmarterPlayer, but excludes moves that would allow the opponent to win if they play on top of it.

- **TeenagerSmarterPlayer**: Same as TeenagerPlayer, but checks if a move creates a line of three tokens with available spaces on both sides. If so, it will play that move.

- **AdultPlayer**: Same as TeenagerSmarterPlayer, but also checks if a move creates a line of three tokens with available spaces on both sides for the opponent. If so, it will play that move to block the opponent.

- **AdultSmarterPlayer**: Same as AdultPlayer, but checks if a move allows to create multiple ways to win and plays that move. Also checks if a move allows the opponent to create multiple ways to win and plays that move to protect itself.

- **ConsolePlayer**: Asks for moves to play in the console. Perfect for testing your own AI.

### Elo Ratings

Here are the Elo ratings of the different algorithms:

```
1. AdultSmarterPlayer:    1767
2. AdultPlayer:           1712
3. MinimaxPlayer depth 3: 1672
4. MinimaxPlayer depth 2: 1622
5. TeenagerSmarterPlayer: 1611
6. TeenagerPlayer:        1604
7. ChildSmarterPlayer:    1525
8. MinimaxPlayer depth 1: 1220
9. ChildPlayer:           1208
10. BabyPlayer:            995
```

In addition to the provided players, we also offer a tool to evaluate the Elo rating of your own AI model. This is extremely useful to have an "absolute" idea of the progress of your AI. For example, if an AI learns by fighting against itself, we know that it is getting stronger as it would be able to win against its older versions, but this is not enough to evaluate if it has learned a lot. This is where our tool comes in, which allows you to give an Elo rating to the AI.

Here is how to use it in Python:

```python
env = ConnectFourEnv(opponent=BabyPlayer())
model = PPO("MlpPolicy", env)
model.learn(total_timesteps=10000)

myModelPlayer = ModelPlayer(model,name="Your trained Model")

your_model_elo = EloLeaderboard().get_elo([myModelPlayer], num_matches=100)
```

You can find an example of how to use this tool in a Google Colab notebook [here](https://colab.research.google.com/github/lucasBertola/Connect-4-env/blob/main/exemples/PPO_MlpPolicy.ipynb).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lucasBertola/Connect-4-env/blob/main/exemples/PPO_MlpPolicy.ipynb)

## Testing

We believe in the importance of testing. That's why we have included a suite of tests in the `test` directory. To run the tests, simply use the command `pytest`.

## Contribute & Support

We warmly welcome contributions from the community. If you have an idea for an improvement or found a bug, don't hesitate to open an issue or submit a pull request. Your input is greatly appreciated, and our project is made better by your participation!

If you find this repository useful, please give it a star!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
