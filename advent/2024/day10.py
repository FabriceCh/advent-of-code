from __future__ import annotations
from utils import read_file, Grid


ar = read_file("2024/input")
# ar = [
#     "89010123",
#     "78121874",
#     "87430965",
#     "96549874",
#     "45678903",
#     "32019012",
#     "01329801",
#     "10456732",
# ]

grid = Grid(ar)
grid.cast_to_int()

trail_heads = []
for val, x, y in grid:
    if val == 0:
        trail_heads.append((x, y))


# part 1
def find_peaks(head_x, head_y):
    peaks = set()
    queue = [(head_x, head_y)]
    while queue:
        x, y = queue.pop()
        height = grid.get(x, y)
        if height == 9:
            peaks.add((x, y))
            continue
        neighbors = grid.get_neighbors_coords(x, y)
        for n in neighbors:
            if grid.get(n[0], n[1]) == height + 1:
                queue.append(n)
    return len(peaks)


total = 0
for head in trail_heads:
    total += find_peaks(head[0], head[1])

print(total)


# part 2
def find_trails(head_x, head_y):
    trails = 0
    queue = [(head_x, head_y)]
    while queue:
        x, y = queue.pop()
        height = grid.get(x, y)
        if height == 9:
            trails += 1
            continue
        neighbors = grid.get_neighbors_coords(x, y)
        for n in neighbors:
            if grid.get(n[0], n[1]) == height + 1:
                queue.append(n)
    return trails


total = 0
for head in trail_heads:
    total += find_trails(head[0], head[1])

print(total)
