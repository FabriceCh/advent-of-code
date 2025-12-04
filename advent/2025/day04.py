from advent.utils.utils import read_file, Grid

ar = read_file("input")
# ar = [
# "..@@.@@@@.",
# "@@@.@.@.@@",
# "@@@@@.@.@@",
# "@.@@@@..@.",
# "@@.@@@@.@@",
# ".@@@@@@@.@",
# ".@.@.@.@@@",
# "@.@@@.@@@@",
# ".@@@@@@@@.",
# "@.@.@@@.@.",
# ]

total = 0
#part 1

grid = Grid(ar)
for v, x, y in grid:
    if v != "@":
        continue
    neigh_coords = grid.get_neighbors_coords(x, y, enable_diag=True)
    n_rolls = 0
    for nc in neigh_coords:
        if grid.get(*nc) == "@":
            n_rolls += 1
    if n_rolls < 4:
        total += 1

print(total)



# part 2
def step(grid):
    n = 0
    to_remove = []
    for v, x, y in grid:
        if v != "@":
            continue
        neigh_coords = grid.get_neighbors_coords(x, y, enable_diag=True)
        n_rolls = 0
        for nc in neigh_coords:
            if grid.get(*nc) == "@":
                n_rolls += 1
        if n_rolls < 4:
            n += 1
            to_remove.append((x, y))
    for v, x, y in grid:
        if (x, y) in to_remove:
            grid.set(x, y, ".")
    return n

ans = 0
finished = False
while not finished:
    print(grid)
    got = step(grid)
    ans += got
    finished = got == 0
    

print(ans)
