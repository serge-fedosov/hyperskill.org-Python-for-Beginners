# impossible = "Impossible"
# draw = "Draw"
# game_not_finished = "Game not finished"
#
#
# def win(v):
#     return a[0] == v and a[1] == v and a[2] == v \
#         or a[3] == v and a[4] == v and a[5] == v \
#         or a[6] == v and a[7] == v and a[8] == v \
#         or a[0] == v and a[3] == v and a[6] == v \
#         or a[1] == v and a[4] == v and a[7] == v \
#         or a[2] == v and a[5] == v and a[8] == v \
#         or a[0] == v and a[4] == v and a[8] == v \
#         or a[2] == v and a[4] == v and a[6] == v
#
#
# def check(s):
#     if win("X") and win("O"):
#         print(impossible)
#         return
#
#     if abs(s.count("X") - s.count("O")) >= 2:
#         print(impossible)
#         return
#
#     if win("X"):
#         print("X wins")
#         return
#     elif win("O"):
#         print("O wins")
#         return
#
#     if s.count("_") == 0:
#         print(draw)
#         return
#
#     print(game_not_finished)

# check(a)

cell_occupied = "This cell is occupied! Choose another one!"
enter_numbers = "You should enter numbers!"
wrong_coordinates = "Coordinates should be from 1 to 3!"


def print_grid(grid):
    print("---------")
    print(f"| {grid[0]} {grid[1]} {grid[2]} |")
    print(f"| {grid[3]} {grid[4]} {grid[5]} |")
    print(f"| {grid[6]} {grid[7]} {grid[8]} |")
    print("---------")


def move(grid):
    while True:
        val_y, val_x = input().split()

        try:
            y = int(val_y)
            x = int(val_x)
        except ValueError:
            print(enter_numbers)
            continue

        if not 1 <= y <= 3 or not 1 <= x <= 3:
            print(wrong_coordinates)
            continue

        if a[3 * (y - 1) + x - 1] != "_":
            print(cell_occupied)
            continue

        grid[3 * (y - 1) + x - 1] = "X"
        return


a = list(input())
print_grid(a)
move(a)
print_grid(a)
