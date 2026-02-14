import json

def get_number():
    """This gets the user number"""
    filename = "my_num.json"
    try:
        with open(filename) as f:
            num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return num

def remember_number():
    """Prompt for a number"""
    nums = input("What is your favorite number? ")
    filename = "my_num.json"

    with open(filename, 'w') as f:
        json.dump(nums, f)
    return nums
    
def print_number():
    """Prints a message with the number"""
    nums = get_number()
    if nums:
        print(f"Your favorite number is, {nums}")
    else:
        nums = get_number()
        print(f"We'll remember you when you come back, {nums}!")

print_number()
