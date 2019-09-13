import random
import re

_TOKENS = ["X", "O"]
_BOARD = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


class Game:

    def __init__(self, user_name):
        self.board = Board()
        self._user = (user_name, random.choice(_TOKENS))
        self._ia_token = "X" if self.get_user_token() == "O" else "O"
        self.current_player = self.get_user_name() if random.choice(_TOKENS) == self.get_user_token() else "IA"

    def make_user_play(self):
        valid_pos = False
        while not valid_pos:
            pos = input("What position do you want to mark?(e.g. '1C or B3'): ").upper()

            valid_pos = self.__check_valid_pos(pos)
            if valid_pos:
                if self.board.is_empty_pos(valid_pos):
                    self.board.set_mark(valid_pos, self.get_user_token())
                    break
                else:
                    print("that position is already marked!")
                    valid_pos = False

    def make_ia_play(self):
        valid_pos = (random.randint(0, 2), random.randint(0, 2))
        while not self.board.is_empty_pos(valid_pos):
            valid_pos = (random.randint(0, 2), random.randint(0, 2))
        self.board.set_mark(valid_pos, self.get_ia_token())

    def change_player_turn(self):
        self.current_player = self.get_user_name() if self.current_player == "IA" else "IA"

    def check_end_of_game(self):
        cp = self.current_player
        cp_tkn = self.get_ia_token() if cp == "IA" else self.get_user_token()

        if self.board.is_full_board():
            msj = "The board is full, this match ends in a Draw! ;)"
        elif self.board.three_aligned(cp_tkn):
            msj = "Game has ended, {} WIN !!!".format(cp)
        else:
            msj = ""
        return msj

    def get_user_name(self):
        return self._user[0]

    def get_user_token(self):
        return self._user[1]

    def get_ia_token(self):
        return self._ia_token

    @staticmethod
    def __check_valid_pos(pos):
        regex = r'([A-C][1-3])|([1-3][A-C])'
        if len(pos) == 2 and re.match(regex, pos):
            base_num = ord("A")
            if pos[0].isdigit():
                return int(pos[0]) - 1, (ord(pos[1]) - base_num)
            return int(pos[1]) - 1, (ord(pos[0]) - base_num)
        else:
            return False


class Board:

    def __init__(self):
        self.board = _BOARD
        self._total_pos = 9
        self._marked_pos = 0

    def get_board(self):
        return self.board

    def set_mark(self, pos, token):
        row, col = pos
        self.board[row][col] = token
        self._marked_pos += 1

    def is_empty_pos(self, pos):
        return self.board[pos[0]][pos[1]] == " "

    def is_full_board(self):
        return self._total_pos == self._marked_pos

    def three_aligned(self, cp_tkn):
        winner = ((self.board[0][0] == cp_tkn and self.board[0][1] == cp_tkn and self.board[0][2] == cp_tkn) or
                  (self.board[1][0] == cp_tkn and self.board[1][1] == cp_tkn and self.board[1][2] == cp_tkn) or
                  (self.board[2][0] == cp_tkn and self.board[2][1] == cp_tkn and self.board[2][2] == cp_tkn) or
                  # horizontal
                  (self.board[0][0] == cp_tkn and self.board[1][0] == cp_tkn and self.board[2][0] == cp_tkn) or
                  (self.board[0][1] == cp_tkn and self.board[1][1] == cp_tkn and self.board[2][1] == cp_tkn) or
                  (self.board[0][2] == cp_tkn and self.board[1][2] == cp_tkn and self.board[2][2] == cp_tkn) or
                  # vertical
                  (self.board[0][0] == cp_tkn and self.board[1][1] == cp_tkn and self.board[2][2] == cp_tkn) or
                  (self.board[0][2] == cp_tkn and self.board[1][1] == cp_tkn and self.board[2][0] == cp_tkn))
        # diagonal
        return winner
