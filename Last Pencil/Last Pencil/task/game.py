names = ["John", "Jack"]

print("How many pencils would you like to use:")
pencils = int(input())

print(f"Who will be the first ({names[0]}, {names[1]}):")
name = input()

player = 0 if name == names[0] else 1
while pencils > 0:
    print("|" * pencils)
    print(f"{names[player]}'s turn:")
    take = int(input())
    pencils -= take
    player = 1 if player == 0 else 0
