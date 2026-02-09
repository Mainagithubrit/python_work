import json

filename = 'my_num.json'

nums = input("What is your favorite number? ")

with open(filename, 'w') as f:
    json.dump(nums, f)
