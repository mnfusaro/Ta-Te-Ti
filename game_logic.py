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
        """Asks the user for a position and validates it.
        Once the position is validated, it is marked on the board.
        """

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
        """Look for a potential user move (two adjacent marked positions) and cancel it.
        If there isn't, it plays randomly.
        """

        board = self.board.get_board()
        valid_pos = (random.randint(0, 2), random.randint(0, 2))

        for pos_r, row in enumerate(board):
            occupied_h = 0
            occupied_v = 0
            occupied_o = 0
            for pos_c, col in enumerate(row):
                if col == self.get_user_token():  # Search for horizontal play
                    occupied_h += 1
                if board[pos_c][pos_r] == self.get_user_token():  # Search for vertical play
                    occupied_v += 1
                if board[pos_c][pos_c] == self.get_user_token():  # Search for diagonal play
                    occupied_o += 1

            if occupied_h == 2 and self.board.is_empty_pos((pos_r, pos_c)):
                valid_pos = pos_r, pos_c
            if occupied_v == 2 and self.board.is_empty_pos((pos_c, pos_r)):
                valid_pos = pos_c, pos_r
            if occupied_o == 2 and self.board.is_empty_pos((pos_c, pos_c)):
                valid_pos = pos_c, pos_c

        while not self.board.is_empty_pos(valid_pos):
            valid_pos = (random.randint(0, 2), random.randint(0, 2))
        self.board.set_mark(valid_pos, self.get_ia_token())

    def change_player_turn(self):
        self.current_player = self.get_user_name() if self.current_player == "IA" else "IA"

    def check_end_of_game(self):
        """check if the board was filled or if any player won.
        :returns A message if this occurs or an empty string if doesn't.
        """
        cp = self.current_player
        cp_tkn = self.get_ia_token() if cp == "IA" else self.get_user_token()

        if self.board.is_full_board():
            msg = "The board is full, this match ends in a Draw! ;)"
        elif self.board.three_aligned(cp_tkn):
            msg = "Game has ended, {} WIN !!!".format(cp)
        else:
            msg = ""
        return msg

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
        """
        :param cp_tkn: Str (a token)
        :return: A boolean that indicates if there are three contiguous positions occupied by a player.
        """
        three_aligned = ((self.board[0][0] == cp_tkn and self.board[0][1] == cp_tkn and self.board[0][2] == cp_tkn) or
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
        return three_aligned
