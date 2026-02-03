filename = 'poll.txt'

with open(filename, 'a') as file_objet:

    while True:
        print("To stop please type 'quit' ")
        # name = input('Please enter your name: ')
        reason = input('Why do you like programing: ')

        """ poll_dict = {}

        poll_dict['name'] = 'name'
        poll_dict['reason'] = 'reason'
        """
        print('\n')
        if reason == 'quit':
            break
        else:
            file_objet.write(reason)
            file_objet.write('\n')
