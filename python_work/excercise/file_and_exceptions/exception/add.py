print("Give me two numbers and I will add them.")
print("Enter 'q' to quit the program." )

while True:
    first_number = input("\nEnter the First Number: ")
    if first_number == 'q':
        break

    second_number = input("Enter the second Number: ")
    if second_number == 'q':
        break

    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print("You can only add two numbers to my program!")
    else:
        print(result)
