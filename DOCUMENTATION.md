# ConnectFourEnv

`ConnectFourEnv` is a class that represents the environment for the Connect Four game. It is built on top of the Gymnasium library and provides methods to interact with the game, such as playing actions, rendering the game state, and checking for valid actions.

## Methods

### `change_opponent(self, opponent)`

Changes the opponent in the environment.

- `opponent`: The new opponent to play against.

### `clone(self)`

Creates a copy of the current environment.

### `clone_and_play(self, action)`

Clones the environment and plays an action in the cloned environment. The board is always in a format to be seen by the next player who has to play (i.e., 1 for the player who is going to play, -1 for their opponent).

- `action`: The action to play in the cloned environment.

### `close(self)`

Closes the environment and any associated resources.

### `get_valid_actions(self)`

Returns a list of valid actions for the current game state.

### `inverse_player_position(self)`

Inverts the player positions on the board.

### `is_action_valid(self, action)`

Checks if an action is valid.

- `action`: The action to check.

### `is_column_full(self, column)`

Checks if a column is full.

- `column`: The column to check.

### `__init__(self, opponent=None, render_mode=None, first_player=None)`

Initializes the Connect Four environment.

- `opponent`: The opponent to play against (default: None).
- `render_mode`: The mode to render the game, either "human" or "rgb_array" (default: None).
- `first_player`: The first player to play, either 1 or -1 (default: None).

### `render(self)`

Renders the game state.

### `reset(self, seed=None, options=None)`

Resets the environment to its initial state.

- `seed`: The random seed for the environment (default: None).
- `options`: Additional options for resetting the environment (default: None).

### `step(self, action, play_opponent=True)`

Performs an action in the environment. The board is always in a format to be seen by the next player who has to play (i.e., 1 for the player who is going to play, -1 for their opponent).

- `action`: The action to perform.
- `play_opponent`: Whether to play the opponent's move after the action (default: True).

### `switch_player(self)`

Switches the current player to play.