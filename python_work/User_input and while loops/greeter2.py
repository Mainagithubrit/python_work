"""This code stores a prompt in a variable for user input"""

prompt = "If you tell us who you are, we can personalize the messages you see."

prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, {}".format(name))