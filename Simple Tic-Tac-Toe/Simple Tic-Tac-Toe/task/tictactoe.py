cell_occupied = "This cell is occupied! Choose another one!"
enter_numbers = "You should enter numbers!"
wrong_coordinates = "Coordinates should be from 1 to 3!"
xo_draw = "Draw"
x_wins = "X wins"
o_wins = "O wins"


def win(grid, v):
    return grid[0] == v and grid[1] == v and grid[2] == v \
        or grid[3] == v and grid[4] == v and grid[5] == v \
        or grid[6] == v and grid[7] == v and grid[8] == v \
        or grid[0] == v and grid[3] == v and grid[6] == v \
        or grid[1] == v and grid[4] == v and grid[7] == v \
        or grid[2] == v and grid[5] == v and grid[8] == v \
        or grid[0] == v and grid[4] == v and grid[8] == v \
        or grid[2] == v and grid[4] == v and grid[6] == v


def draw(grid):
    return grid.count(" ") == 0


def print_grid(grid):
    print("---------")
    print(f"| {grid[0]} {grid[1]} {grid[2]} |")
    print(f"| {grid[3]} {grid[4]} {grid[5]} |")
    print(f"| {grid[6]} {grid[7]} {grid[8]} |")
    print("---------")


def move(grid, value):
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

        if grid[3 * (y - 1) + x - 1] != " ":
            print(cell_occupied)
            continue

        grid[3 * (y - 1) + x - 1] = value
        return


player = "X"
a = [" "] * 9
print_grid(a)

while not win(a, "X") and not win(a, "O") and not draw(a):
    move(a, player)
    print_grid(a)
    player = "X" if player == "O" else "O"

if win(a, "X"):
    print(x_wins)
elif win(a, "O"):
    print(o_wins)
else:
    print(xo_draw)
