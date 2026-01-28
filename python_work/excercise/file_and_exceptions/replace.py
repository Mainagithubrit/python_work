filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in range(3):
    for line in lines:
        for i in line:
            if i == 'Python':
                i.replace('Python', 'JavaScript')
                print(line.rstrip())

    print("\n")
