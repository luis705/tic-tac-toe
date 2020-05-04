import time

table = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

points_table = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]


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


def show_table():

    print('  |  |  \n'
          '--|--|--\n'
          '  |  |  \n'
          '--|--|--\n'
          '  |  |  \n')


def tutorial():
    print(' 1 | 2 | 3 \n'
          '---|---|---\n'
          ' 4 | 5 | 6 \n'
          '---|---|---\n'
          ' 7 | 8 | 9 \n')
    print('Type the number of the spot you want to put your piece')


while True:
    menu()
    choice = input()

    if choice == '1':
        pass
    elif choice == '2':
        tutorial()
        time.sleep(2)
    elif choice == '3':
        break
    else:
        print("You must type 1, 2 or 3")
