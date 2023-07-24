import numpy as np
from .Player import Player

class MinMaxPlayer(Player):
    def __init__(self, depth=2):
        self.depth = depth

    def play(self, observation):
        _, best_moves = self.minimax(observation, self.depth, True)
        best_move = np.random.choice(best_moves)

        if best_move is None or observation[0, best_move] != 0:
            valid_moves = [c for c in range(7) if observation[0, c] == 0]
            best_move = np.random.choice(valid_moves)

        return best_move

    def getName(self):
        return f"MinimaxPlayer depth {self.depth}"

    def getElo(self):
        return None
    
    def isDeterministic(self):
        return False

    def minimax(self, board, depth, maximizing_player):
        if depth == 0 or self.is_terminal_node(board):
            evaluation = self.evaluate_board(board)
            return evaluation, []

        valid_moves = [c for c in range(7) if board[0, c] == 0]

        best_moves = []
        if maximizing_player:
            value = float('-inf')
            for move in valid_moves:
                new_board = self.apply_move(board, move, 1)
                new_value, _ = self.minimax(new_board, depth - 1, False)
                if new_value > value:
                    value = new_value
                    best_moves = [move]
                elif new_value == value:
                    best_moves.append(move)
            return value, best_moves
        else:
            value = float('inf')
            for move in valid_moves:
                new_board = self.apply_move(board, move, 2)
                new_value, _ = self.minimax(new_board, depth - 1, True)
                if new_value < value:
                    value = new_value
                    best_moves = [move]
                elif new_value == value:
                    best_moves.append(move)
            return value, best_moves

    def apply_move(self, board, move, player):
        new_board = board.copy()
        for i in range(5, -1, -1):
            if new_board[i, move] == 0:
                new_board[i, move] = player
                break
        return new_board

    def is_terminal_node(self, board):
        return self.check_win(board, 1) or self.check_win(board, 2) or np.all(board != 0)

    def check_win(self, board, player):
        for i in range(6):
            for j in range(4):
                if (board[i, j:j+4] == player).all():
                    return True
        for i in range(3):
            for j in range(7):
                if (board[i:i+4, j] == player).all():
                    return True
        for i in range(3):
            for j in range(4):
                if (board[i:i+4, j:j+4].diagonal() == player).all():
                    return True
                if (board[i:i+4, j:j+4][::-1].diagonal() == player).all():
                    return True
        return False

    def evaluate_board(self, board):
        player1_max_sequence = self.check_win(board, 1)
        player2_max_sequence = self.check_win(board, 2)

        if player1_max_sequence:
            return float('inf')
        elif player2_max_sequence:
            return float('-inf')
        else:
            return 0

    def max_aligned_tokens(self, board, player):
        max_sequence = 0

        for i in range(6):
            for j in range(4):
                sequence = np.sum(board[i, j:j+4] == player)
                max_sequence = max(max_sequence, sequence)

        for i in range(3):
            for j in range(7):
                sequence = np.sum(board[i:i+4, j] == player)
                max_sequence = max(max_sequence, sequence)

        for i in range(3):
            for j in range(4):
                sequence = np.sum(board[i:i+4, j:j+4].diagonal() == player)
                max_sequence = max(max_sequence, sequence)
                sequence = np.sum(board[i:i+4, j:j+4][::-1].diagonal() == player)
                max_sequence = max(max_sequence, sequence)

        return max_sequence