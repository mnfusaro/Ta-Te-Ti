import random

TOKENS = ["X", "O"]
_BOARD = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


class Game:

    def __init__(self):
        self.board = _Board()
        self.user_token = random.choice(TOKENS)
        self.ia_token = "X" if self.user_token == "O" else "O"

    def make_user_play(self, pos):
        pass

    def make_ia_play(self):
        pass


class _Board:

    def __init__(self):
        self.board = _BOARD

    def get_board(self):
        return self.board

    def set_mark(self, pos, token):
        row, col = pos
        self.board[row][col] = token
