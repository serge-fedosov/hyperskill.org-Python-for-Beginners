impossible = "Impossible"
draw = "Draw"
game_not_finished = "Game not finished"

def win(v):
    return a[0] == v and a[1] == v and a[2] == v \
        or a[3] == v and a[4] == v and a[5] == v \
        or a[6] == v and a[7] == v and a[8] == v \
        or a[0] == v and a[3] == v and a[6] == v \
        or a[1] == v and a[4] == v and a[7] == v \
        or a[2] == v and a[5] == v and a[8] == v \
        or a[0] == v and a[4] == v and a[8] == v \
        or a[2] == v and a[4] == v and a[6] == v


def check(s):
    if win("X") and win("O"):
        print(impossible)
        return

    if abs(s.count("X") - s.count("O")) >= 2:
        print(impossible)
        return

    if win("X"):
        print("X wins")
        return
    elif win("O"):
        print("O wins")
        return

    if s.count("_") == 0:
        print(draw)
        return

    print(game_not_finished)


a = input()

print("---------")
print(f"| {a[0]} {a[1]} {a[2]} |")
print(f"| {a[3]} {a[4]} {a[5]} |")
print(f"| {a[6]} {a[7]} {a[8]} |")
print("---------")

check(a)
