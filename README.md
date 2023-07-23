# Connect Four Environment

Welcome to the Connect Four Environment repository!
This is a versatile and engaging environment designed for reinforcement learning agents. 
The goal of the game is to connect four of your own pieces in a row, either horizontally, vertically, or diagonally, while preventing your opponent from doing the same.
The environment can be used with both Fully Connected Networks (FCN) and Convolutional Neural Networks (CNN).

## Features

- **Customizable Board Size**: You can easily adjust the size of the board to challenge your agent with different levels of complexity.
- **FCN and CNN Compatible**: The environment is designed to work seamlessly with both FCN and CNN policies. This makes it a great playground to experiment with different types of neural networks.
- **Human Render Mode**: Watch your agent learn in real-time with the human render mode. It's not just about the numbers, it's also about the journey!
- **Two-Player Mode**: Train your agent against another AI or even a human opponent to test its performance in real-world scenarios.
- **OpenAI Gym / Gymnasium Compatible**: Connect Four follows the OpenAI Gym / Gymnasium interface, making it compatible with a wide range of reinforcement learning libraries and algorithms.


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
1.  AdultSmarterPlayer:    1767
2.  MinimaxPlayer depth 3: 1710
3.  AdultPlayer:           1689
4.  TeenagerSmarterPlayer: 1664
5.  TeenagerPlayer:        1644
6.  MinimaxPlayer depth 2: 1596
7.  ChildSmarterPlayer:    1548
8.  ChildPlayer:           1223
9.  MinimaxPlayer depth 1: 1174
10. BabyPlayer:             985
```

In addition to the provided players, we also offer a tool to evaluate the Elo rating of your own AI model. This is extremely useful to have an "absolute" idea of the progress of your AI. For example, if an AI learns by fighting against itself, we know that it is getting stronger as it would be able to win against its older versions, but this is not enough to evaluate if it has learned a lot. This is where our tool comes in, which allows you to give an Elo rating to the AI.

Here is how to use it in Python:

```python
env = ConnectFourEnv(opponent=BabyPlayer())
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

myModelPlayer = ModelPlayer(model,name="Your trained Model")

players = [
    BabyPlayer(),
    ChildPlayer(),
    ChildSmarterPlayer(),
    TeenagerPlayer(),
    myModelPlayer
]

elo_leaderboard = EloLeaderboard(players)
elo_leaderboard.play_and_display(num_matches=10)
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

Todo 
- readme
- test
- pip
- exemple
- exemple with jupiter
- bot readme
- benchmark perf with bot 
- readme for using of elo leadeerboard
- working with conv network
- readme: tester son ia
