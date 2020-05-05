import time
from auxiliary_functions import *


table = [[' ' for i in range(3)] for j in range(3)]
points_table = [[0 for i in range(3)] for j in range(3)]
curr_player = 1


def play(player, table, points_table):
    place = input()
    if player == 1:
        if place == '1':
            if points_table[0][0] == 0:
                points_table[0][0] = 1
                table[0][0] = 'X'
            else:
                print("That's not a valid place!!!")
                play(player, table, points_table)
        elif place == '2':
            if points_table[0][1] == 0:
                points_table[0][1] = 1
                table[0][1] = 'X'

            else:
                print("That's not a valid place!!!")
                play(player, table, points_table)
        elif place == '3':
            if points_table[0][2] == 0:
                points_table[0][2] = 1
                table[0][2] = 'X'

            else:
                print("That's not a valid place!!!")
                play(player, table, points_table)
        elif place == '4':
            if points_table[1][0] == 0:
                points_table[1][0] = 1
                table[1][0] = 'X'

            else:
                print("That's not a valid place!!!")
                play(player, table, points_table)
        elif place == '5':
            if points_table[1][1] == 0:
                points_table[1][1] = 1
                table[1][1] = 'X'

            else:
                print("That's not a valid place!!!")
                play(player, table, points_table)
        elif place == '6':
            if points_table[1][2] == 0:
                points_table[1][2] = 1
                table[1][2] = 'X'

            else:
                print("That's not a valid place!!!")
                play(player, table, points_table)
        elif place == '7':
            if points_table[2][0] == 0:
                points_table[2][0] = 1
                table[2][0] = 'X'
            else:
                print("That's not a valid place!!!")
                play(player, table, points_table)
        elif place == '8':
            if points_table[2][1] == 0:
                points_table[2][1] = 1
                table[2][1] = 'X'
            else:
                print("That's not a valid place!!!")
                play(player, table, points_table)
        elif place == '9':
            if points_table[2][2] == 0:
                points_table[2][2] = 1
                table[2][2] = 'X'

            else:
                print("That's not a valid place!!!")
                play(player, table, points_table)
        else:
            print("That's not a valid place!!!")
            play(player, table, points_table)
    if player == 2:
        if place == '1':
            if points_table[0][0] == 0:
                points_table[0][0] = -1
                table[0][0] = 'O'
        elif place == '2':
            if points_table[0][1] == 0:
                points_table[0][1] = -1
                table[0][1] = 'O'
            else:
                print("That's not a valid place!!!")
                play(player, table, points_table)
        elif place == '3':
            if points_table[0][2] == 0:
                points_table[0][2] = -1
                table[0][2] = 'O'
            else:
                print("That's not a valid place!!!")
                play(player, table, points_table)
        elif place == '4':
            if points_table[1][0] == 0:
                points_table[1][0] = -1
                table[1][0] = 'O'
            else:
                print("That's not a valid place!!!")
                play(player, table, points_table)
        elif place == '5':
            if points_table[1][1] == 0:
                points_table[1][1] = -1
                table[1][1] = 'O'
            else:
                print("That's not a valid place!!!")
                play(player, table, points_table)
        elif place == '6':
            if points_table[1][2] == 0:
                points_table[1][2] = -1
                table[1][2] = 'O'
            else:
                print("That's not a valid place!!!")
                play(player, table, points_table)
        elif place == '7':
            if points_table[2][0] == 0:
                points_table[2][0] = -1
                table[2][0] = 'O'
            else:
                print("That's not a valid place!!!")
                play(player, table, points_table)
        elif place == '8':
            if points_table[2][1] == 0:
                points_table[2][1] = -1
                table[2][1] = 'O'
            else:
                print("That's not a valid place!!!")
                play(player, table, points_table)
        elif place == '9':
            if points_table[2][2] == 0:
                points_table[2][2] = -1
                table[2][2] = 'O'
            else:
                print("That's not a valid place!!!")
                play(player, table, points_table)
        else:
            print("That's not a valid place!!!")
            play(player, table, points_table)


def game(computer):
    #  Function that creates the game between two players
    global curr_player
    global table
    global points_table

    while True:
        print(f"Player's {curr_player} turn, where do you want to put your piece?")
        show_table(table)
        play(curr_player, table, points_table)
        if curr_player == 1:
            curr_player = 2
        else:
            curr_player = 1

        if winner(points_table) != 0:
            print(f'Congratulations Player {winner(points_table)}!')
            table = [[' ' for i in range(3)] for j in range(3)]
            points_table = [[0 for i in range(3)] for j in range(3)]
            curr_player = 1
            break
        if is_finished(points_table):
            table = [[' ' for i in range(3)] for j in range(3)]
            points_table = [[0 for i in range(3)] for j in range(3)]
            curr_player = 1
            break
        time.sleep(.5)


while True:
    choice = menu()

    if choice == '1':
        mode = game_modes()
        if mode == '1':
            game(1)
        if mode == '2':
            game(0)

    elif choice == '2':
        show_table([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print("Type the number of the place you want to pay")
        time.sleep(2)
    elif choice == '3':
        break
