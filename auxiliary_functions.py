import copy

x_square = 'X'
o_square = 'O'

o_wins = 'O wins!'
x_wins = 'X wins!'
draw = 'Draw!'

table = [[' ' for i in range(3)] for j in range(3)]


def winner(table):
    potential_wins = []

    # Look in the table for three in a row
    for row in table:
        potential_wins.append(list(row))

    #  Three in a column
    for i in range(3):
        potential_wins.append(list([table[j][i] for j in range(3)]))

    #  Three in a diagonal
    potential_wins.append(list(table[i][i] for i in range(3)))
    potential_wins.append(list(table[i][2 - i] for i in range(3)))

    #  Checking if any three are the same
    for trio in potential_wins:
        if trio == ['X', 'X', 'X']:
            return x_wins
        elif trio == ['O', 'O', 'O']:
            return o_wins
    return 0


def is_finished(table):
    if ' ' in table[0] or ' ' in table[1] or ' ' in table[2]:
        return False
    return True


def show_table(table):

    print(f' {table[0][0]} | {table[0][1]} | {table[0][2]} \n'
          '---|---|---\n'
          f' {table[1][0]} | {table[1][1]} | {table[1][2]} \n'
          '---|---|---\n'
          f' {table[2][0]} | {table[2][1]} | {table[2][2]} \n')



def menu():
    #  Function to print the game menu

    print('/-------------------\ \n'
          '|                   |\n'
          '|     MAIN MENU     |\n'
          '|                   |\n'
          '|  1 - New Game     |\n'
          '|  2 - Instructions |\n'
          '|  3 - Close        |\n'
          '|                   |\n'
          '\-------------------/')

    #  Choice validation
    while True:
        choice = input()

        if choice != '1' and choice != '2' and choice != '3':
            print('You must type 1, 2 or 3')
        else:
            return choice


def choice_to_table(choice):
    choice = int(choice)
    if 1 <= choice <= 3:
        return [0, choice - 1]
    if 4 <= choice <= 6:
        return [1, choice - 4]
    if 7 <= choice <= 9:
        return [2, choice - 7]


def is_x_turn(table):
    count = 0
    for row in table:
        count += table.count(x_square)
        count -= table.count(o_square)
    return count == 0


def play(table, player):

    #  Get the player choice
    place = input()
    indexes = choice_to_table(place)

    if player == 1:
        if table[indexes[0]][indexes[1]] == ' ':
            table[indexes[0]][indexes[1]] = x_square
        else:
            print("That's not a valid place!")
            play(table)
    else:
        if table[indexes[0]][indexes[1]] == ' ':
            table[indexes[0]][indexes[1]] = o_square
        else:
            print("That's not a valid place!")
            play(table)


def game():

    global table
    player = 1

    while True:

        print(f"Player's {player} turn, where do you want to put your piece?")
        show_table(table)
        play(table, player)

        if player == 1:
            player = 2
        else:
            player = 1

        if winner(table) != 0:
            print(winner(table))
            table = [[' ' for i in range(3)] for j in range(3)]
            break

        if is_finished(table):
            print('Draw!')
            table = [[' ' for i in range(3)] for j in range(3)]
            break




