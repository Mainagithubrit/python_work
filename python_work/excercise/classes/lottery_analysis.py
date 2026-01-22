from lottery import *

def check_ticket():
    my_ticket = ['c', 'e', 10, 5]
    loop = 0

    while True:
        if winning_lottery == my_ticket:
            print(f'Your ticket {my_ticket} won!')
            break
        else:
            print(f"Your ticket {my_ticket} did not win!\n")

            loop +=1
            print(loop)

check_ticket()
