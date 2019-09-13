from string import ascii_uppercase
import time

from game_logic import Game


def draw_board(board):
    print("   ", end="")
    for num in range(len(board)):  # print the horizontal reference frame
        print(ascii_uppercase[num], end=' ')
    print()
    print("  -------")

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

    draw_board(game.board.get_board())

    while True:

        print("It's {} turn".format(game.current_player))

        if game.current_player == game.get_user_name():
            game.make_user_play()
        else:
            print("...")
            time.sleep(2)
            game.make_ia_play()

        draw_board(game.board.get_board())
        print("\n" * 2)

        game_ended = game.check_end_of_game()
        if game_ended:
            print("{}".format(game_ended))
            break
        else:
            game.change_player_turn()


if __name__ == '__main__':
    main()
