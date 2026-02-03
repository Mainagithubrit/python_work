filename = 'guest_book.txt'

with open(filename, 'a') as file_objet:

    while True:
        print("To stop please type 'quit' ")
        name = input('Please enter your name: ')

        if name == 'quit':
            break
        else:
            print(f"\nHey {name}, Welcome to my guest book!\n")

            file_objet.write(name)
            file_objet.write('\n')
