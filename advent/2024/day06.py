from utils import read_file, Grid

ar = read_file("2024/input")
# ar = [
#     "....#.....",
#     ".........#",
#     "..........",
#     "..#.......",
#     ".......#..",
#     "..........",
#     ".#..^.....",
#     "........#.",
#     "#.........",
#     "......#...",
# ]
ar = [[c for c in line] for line in ar]
grid = Grid(ar)

# part 1
nav_x, nav_y = 0, 0
for c, x, y in grid:
    if c in ["^", "<", ">", "v"]:
        nav_x, nav_y = x, y

DIRECTIONS = ["N", "E", "S", "W"]


def rotate(dir) -> int:
    return (dir + 1) % 4


facing = 0

while not grid.is_out_of_bounds(nav_x, nav_y):
    if grid.get(nav_x, nav_y) != "^":
        grid.set(nav_x, nav_y, "X")
    next_x, next_y = 0, 0
    if DIRECTIONS[facing] == "N":
        next_x, next_y = grid.get_north_coord(nav_x, nav_y)
    elif DIRECTIONS[facing] == "E":
        next_x, next_y = grid.get_east_coord(nav_x, nav_y)
    elif DIRECTIONS[facing] == "S":
        next_x, next_y = grid.get_south_coord(nav_x, nav_y)
    elif DIRECTIONS[facing] == "W":
        next_x, next_y = grid.get_west_coord(nav_x, nav_y)

    if not grid.is_out_of_bounds(next_x, next_y) and grid.get(next_x, next_y) == "#":
        facing = rotate(facing)
    else:
        nav_x, nav_y = next_x, next_y

count = 0
for c, _, _ in grid:
    if c == "X":
        count += 1

print(count + 1)


# part 2
def is_looping(grid) -> bool:
    nav_x, nav_y = 0, 0
    visited = set()
    for c, x, y in grid:
        if c in ["^", "<", ">", "v"]:
            nav_x, nav_y = x, y

    facing = 0

    while not grid.is_out_of_bounds(nav_x, nav_y):
        if (nav_x, nav_y, facing) in visited:
            return True
        visited.add((nav_x, nav_y, facing))
        next_x, next_y = 0, 0
        if DIRECTIONS[facing] == "N":
            next_x, next_y = grid.get_north_coord(nav_x, nav_y)
        elif DIRECTIONS[facing] == "E":
            next_x, next_y = grid.get_east_coord(nav_x, nav_y)
        elif DIRECTIONS[facing] == "S":
            next_x, next_y = grid.get_south_coord(nav_x, nav_y)
        elif DIRECTIONS[facing] == "W":
            next_x, next_y = grid.get_west_coord(nav_x, nav_y)

        if (
            not grid.is_out_of_bounds(next_x, next_y)
            and grid.get(next_x, next_y) == "#"
        ):
            facing = rotate(facing)
        else:
            nav_x, nav_y = next_x, next_y
    return False


count = 0
for c, x, y in grid:
    if c == "." or c == "X":
        new_grid = Grid(grid._grid)
        new_grid.set(x, y, "#")
        count += is_looping(new_grid)
        new_grid.set(x, y, ".")

print("part2 finished: answer should be 6 for test input")
print(count)
