"""This Program uses a flag to check if a condition is true or false"""

prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\n Enter 'quit' to end the program "

active = True
while active:
    message = input(prompt)
    
    if message == "quit":
        active = False
    else:
        print(message)