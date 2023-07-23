# Connect-4-env

## Available Players

You can integrate players as opponents in your gym environment like this:

```python
env = ConnectFourEnv(opponent=BabyPlayer())
```

### Player Descriptions

- **MinimaxPlayer**: An implementation of the Minimax algorithm. Can be used with different search depths (e.g., `MinimaxPlayer(depth=3)`), but it is very slow, so it is not recommended for general use. All other algorithms are much faster.

- **BabyPlayer**: Plays random moves.

- **ChildPlayer**: Plays random moves, but if there is a winning move, it will play it.

- **ChildSmarterPlayer**: Same as ChildPlayer, but if there is a move that would make the opponent win, it will play that move to block the opponent.

- **TeenagerPlayer**: Same as ChildSmarterPlayer, but excludes moves that would allow the opponent to win if they play on top of it.

- **TeenagerSmarterPlayer**: Same as TeenagerPlayer, but checks if a move creates a line of three tokens with available spaces on both sides. If so, it will play that move.

- **AdultPlayer**: Same as TeenagerSmarterPlayer, but also checks if a move creates a line of three tokens with available spaces on both sides for the opponent. If so, it will play that move to block the opponent.

- **AdultSmarterPlayer**: Same as AdultPlayer, but checks if a move allows the opponent to create multiple ways to win and plays that move. Also checks if a move allows the player to create multiple ways to win and plays that move to protect itself.

- **ConsolePlayer**: Asks for moves to play in the console. Perfect for testing your own AI.

## Elo Ratings

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