"""This is a program that prompts a user to enter their age and get the price to pay"""

prompt = "\nEnter your age and get the price for a movie ticket "

age = input(prompt)
age = int(age)

if age <= 3:
    price = "free"
elif age > 3 and age <= 12:
    price = "$10"
elif age > 12:
    price = "$15"
else:
    ("Input incorrect!!!!")

print("\nYour age is {} and price for a ticket is {}".format(age, price))