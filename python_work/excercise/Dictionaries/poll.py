#!/usr/bin/env python3
"""This code checks to see whether individuals have taken polls"""

polls = {
    'maina': 'python',
    'linet': 'javascript',
    'gitau': 'javascript',
    'jack': 'css',
    'olwal': 'go',
    'ngugi': 'go',
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

non_polls = ['kim', 'shi', 'shiko', 'travis', 'jen']
for key, value in polls.items(): 
    print("Thank you {}, for taking the poll and choosing {} as a favorite language.\n".format(key.title(), value.title()))

for poll in non_polls:
    if poll not in polls.keys():
        print("{}, Kindly choose your favorite language.".format(poll.title()))
    else:
        print("\n{} you have already chosen a favorite language".format(poll.title()))