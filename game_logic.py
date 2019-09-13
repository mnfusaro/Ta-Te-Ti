import random

_TOKENS = ["X", "O"]
_BOARD = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


class Game:

    def __init__(self, user_name):
        self.board = Board()
        self._user = (user_name, random.choice(_TOKENS))
        self.ia_token = "X" if self.get_user_token() == "O" else "O"
        self.current_player = self.get_user_name() if random.choice(_TOKENS) == self.get_user_token() else "ia"

    def make_user_play(self):
        pass

    def make_ia_play(self):
        pass

    def change_player_turn(self):
        pass

    def check_end_of_game(self):
        pass

    def get_user_name(self):
        pass

    def get_user_token(self):
        pass


class Board:

    def __init__(self):
        self.board = _BOARD

    def get_board(self):
        return self.board

    def set_mark(self, pos, token):
        row, col = pos
        self.board[row][col] = token
