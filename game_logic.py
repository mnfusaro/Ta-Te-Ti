import random


BOARD_SIZE = 3
TOKENS = ["X", "O"]


class Game():
    
    
    def __init__(self):
        self.board = _Board().generate_board()
        self.user_token = random.choice(TOKENS)
        self.ia_token = "X" if self.user_token == "O" else "O"


    def make_user_play(self, pos):
        pass


    def make_ia_play(self):
        pass


class _Board():


    def __init__(self):
        self.board = []

    
    def get_board(self):
        pass

    
    def generate_board(self):
        pass

    
    def set_mark(self, pos):
        pass



