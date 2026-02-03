filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    replce = line.replace('Python', 'Javascript')

    print(replce.rstrip())
