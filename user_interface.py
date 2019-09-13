from game_logic import Game
from shutil import get_terminal_size
from string import ascii_uppercase


def draw_board(board):
    print("   ", end="")
    for num in range(len(board)):  # print the horizontal reference frame
        print(ascii_uppercase[num], end=' ')
    print()

    h_ref = 0
    for row in board:
        h_ref += 1
        print(h_ref, end=" |")  # print the vertical reference frame
        for col in row:
            print(col, end="|")  # print the contents of the board
        print()
        print("  -------")


def main():
    print("Welcome to the game Ta-Te-Ti!")

    game = Game(input("Please enter your name: "))

    print("You will play with '{}'\n".format(game.get_user_token()))

    current_user = game.current_player
    draw_board(game.board.get_board())

    while False:

        print("It's {} turn".format(current_user))

        if current_user == game.get_user_name():
            game.make_user_play()
        else:
            game.make_ia_play()

        print("\n" * get_terminal_size().lines, end='')

        draw_board(game.board.get_board())

        game_ended = game.check_end_of_game()
        if game_ended:
            print("The game is over!")
            print("{}".format(game_ended["msj"]))
            break
        else:
            game.change_player_turn()


main()
