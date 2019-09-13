from game_logic import Game
from shutil import get_terminal_size


def draw_board(board):
    print("ESTE ES EL TABLERO")
    pass


def main():

    print("Welcome to the game Ta-Te-Ti!")
    user_name = input("Please enter your name: ")

    game = Game(user_name)

    print("You will play with '{}'\n".format(game.get_user_token()))

    current_user = game.current_player
    draw_board(game.board.get_board())

    while True:

        print("It's {} turn".format(current_user))

        if current_user == "user":
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
