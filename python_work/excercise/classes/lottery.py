from random import choice

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']


winning_lottery = []


for i in range(4):
    rand = choice(lottery)
    winning_lottery.append(rand)

for win_lot in winning_lottery:
    print(f"\nWinning lottery is: {win_lot}" )

print("\nTodays winning lottery number and letters are: ")
print(winning_lottery)
