def cats_dogs(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # print("Sorry, the file is not found")
        pass
    else:
        if filename == 'cats.txt':
            print('\nThis are cat names:')
            print(contents)
        elif filename == 'dogs.txt':
            print(f'These are dog names:')
            print(contents)

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    cats_dogs(filename)
