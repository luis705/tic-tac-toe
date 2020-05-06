import time
from auxiliary_functions import *

while True:
    choice = menu()

    if choice == '1':
        game()
    elif choice == '2':
        show_table([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print("Type the number of the place you want to pay")
        time.sleep(2)
    elif choice == '3':
        print("Thank you for playing!")
        break




