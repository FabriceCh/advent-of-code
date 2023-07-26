from aocd import get_data
ar = get_data(day=8, year=2022)
ar = ar.splitlines()

ar2 = [ "30373",
        "25512",
        "65332",
        "33549",
        "35390",
]

grid = [list(a) for a in ar]

def is_visible(x, y):
    if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[0]) - 1:
        return True
    value = grid[x][y]
    v1, v2, v3, v4 = True, True, True, True
    for i in range(x):
        if grid[i][y] >= value:
            v1 = False
    for i in range(x+1, len(grid)):
        if grid[i][y] >= value:
            v2 = False
    for i in range(y):
        if grid[x][i] >= value:
            v3 = False
    for i in range(y+1, len(grid[0])):
        if grid[x][i] >= value:
            v4 = False
    return v1 or v2 or v3 or v4

count = 0
for i, _ in enumerate(grid):
    for j, _ in enumerate(grid[0]):
            count += is_visible(i, j)

def part2(x, y):
    if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[0]) - 1:
        return 0
    value = grid[x][y]
    v1, v2, v3, v4 = x, len(grid) - x - 1, y, len(grid) - y - 1

    for i in range(x-1, 0, -1):
        if grid[i][y] >= value:
            v1 = x-i
            break

    for i in range(x+1, len(grid)):
        if grid[i][y] >= value:
            v2 = i-x
            break

    for i in range(y-1, 0, -1):
        if grid[x][i] >= value:
            v3 = y-i
            break

    for i in range(y+1, len(grid[0])):
        if grid[x][i] >= value:
            v4 = i-y
            break

    return v1 * v2 * v3 * v4

#print(part2(1, 2))
#print(part2(3, 2))

mx = 0
for i, _ in enumerate(grid):
    for j, _ in enumerate(grid[0]):
        print(part2(i, j))
        mx = max(mx, part2(i, j))

print(mx)
