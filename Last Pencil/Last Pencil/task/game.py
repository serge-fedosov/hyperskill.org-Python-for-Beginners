import string

names = ["John", "Jack"]

how_many_pencils = "How many pencils would you like to use:"
number_not_numeric = "The number of pencils should be numeric"
number_not_positive = "The number of pencils should be positive"
who_first = "Who will be the first ({}, {}):"
pencil = "|"
turn = "{}'s turn:"
choose_between = "Choose between {} and {}"
possible_values = "Possible values: '1', '2' or '3'"
too_many = "Too many pencils were taken"
won = "{} won!"


def get_pencils():
    while True:
        print(how_many_pencils)
        val = input()

        error = False
        for v in val:
            if v not in string.digits:
                error = True
                break

        if error:
            print(number_not_numeric)
            continue

        n = int(val)
        if n == 0:
            print(number_not_positive)
            continue

        return n


def choose_player():
    print(who_first.format(names[0], names[1]))
    while True:
        name = input()
        if name == names[0]:
            return 0
        elif name == names[1]:
            return 1

        print(choose_between.format(names[0], names[1]))


def take_pencils(max_pencils):
    while True:
        val = input()
        if val not in ["1", "2", "3"]:
            print(possible_values)
            continue

        n = int(val)

        if n > max_pencils:
            print(too_many)
            continue

        return n


pencils = get_pencils()
player = choose_player()

while pencils > 0:
    print(pencil * pencils)
    print(turn.format(names[player]))
    pencils -= take_pencils(pencils)
    player = 1 if player == 0 else 0

print(won.format(names[player]))
