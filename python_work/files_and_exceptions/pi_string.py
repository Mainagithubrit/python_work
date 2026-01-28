filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string +=line.strip()

birthdate = input("Enter your birthday, in the form mmddyy: ")
if birthdate in pi_string:
    print("Your birthdate appears in the first million digits of pi!")
else:
    print("Your birthdate does not appear in the first million digits of pi")
