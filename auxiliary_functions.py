def winner(table):

    if sum(table[0]) == 3 or sum(table[1]) == 3 or sum(table[2]) == 3\
            or table[0][0] + table[1][0] + table[2][0] == 3\
            or table[0][1] + table[1][1] + table[2][1] == 3\
            or table[0][2] + table[1][2] + table[2][2] == 3\
            or table[0][0] + table[1][1] + table[2][2] == 3\
            or table[0][2] + table[1][1] + table[2][0] == 3:
        return 1
    elif sum(table[0]) == 6 or sum(table[1]) == 6 or sum(table[2]) == -3\
            or table[0][0] + table[1][0] + table[2][0] == -3\
            or table[0][1] + table[1][1] + table[2][1] == -3\
            or table[0][2] + table[1][2] + table[2][2] == -3\
            or table[0][0] + table[1][1] + table[2][2] == -3\
            or table[0][2] + table[1][1] + table[2][0] == -3:
        return 2
    else:
        return 0


def is_finished(table):
    if 0 in table[0] or 0 in table[1] or 0 in table[2]:
        return False
    return True


def show_table(table):

    print(f' {table[0][0]} | {table[0][1]} | {table[0][2]} \n'
          '---|---|---\n'
          f' {table[1][0]} | {table[1][1]} | {table[1][2]} \n'
          '---|---|---\n'
          f' {table[2][0]} | {table[2][1]} | {table[2][2]} \n')


def game_modes():
    print('/--------------------\ \n'
          '|                    |\n'
          '|  Choose game mode  |\n'
          '|   1 - 1 player     |\n'
          '|   2 - 2 players    |\n'
          '|                    |\n'
          '\--------------------/')

    while True:
        mode = input()

        if mode != '1' and mode != '2':
            print('You must choose between 1 and 2')
        else:
            return mode


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
