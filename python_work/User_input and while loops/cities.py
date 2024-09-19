"""A program that aks a user about places they have visited.
We use a break to break a while loop regardless of condition"""

prompt = "\nPlease enter the name of a City you have visited."
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print("I'd love to go to {}".format(city))