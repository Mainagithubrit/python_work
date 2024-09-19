"""This program prompts user to enter pizza toppings"""

prompt = "\nPlease enter pizza toppings"
prompt += "\nType 'quit' to end the program: "

while True:
    topping = input(prompt)
    
    if topping == "quit":
        break
    else:
        print("\nYou have added {} to your pizza.".format(topping.title()))