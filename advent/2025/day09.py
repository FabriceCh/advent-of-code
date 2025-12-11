from functools import cache
from types import new_class
from advent.utils.utils import printer, read_file

ar = read_file("input")

TESTING = True
if TESTING:
    ar = read_file("input_test")

def process_input():
    items = []
    for line in ar:
        if line == "":
            break
        items.append([int(i) for i in line.split(",")])
    return items

def area(t1, t2):
    return abs(t1[1] - t2[1] + 1) * abs(t1[0] - t2[0] + 1)

# @printer
def part1():
    tiles = process_input()
    mx = 0
    for i in range(len(tiles)):
        for j in range(i, len(tiles)):
            mx = max(mx, area(tiles[i], tiles[j]))
    return mx

def reduce_dims(tiles):
    x_old_to_new = {}
    y_old_to_new = {}
    x_new_to_old = {}
    y_new_to_old = {}
    sorted_x = sorted(tiles, key=lambda t: t[0])
    sorted_y = sorted(tiles, key=lambda t: t[1])
    i = 0
    for tile in sorted_x:
        x_old = tile[0]
        if x_old not in x_old_to_new:
            x_old_to_new[x_old] = i
            x_new_to_old[i] = x_old
            i += 1

    i = 0
    for tile in sorted_y:
        y_old = tile[1]
        if y_old not in y_old_to_new:
            y_old_to_new[y_old] = i
            y_new_to_old[i] = y_old
            i += 1

    new_tiles = [transform_tile(t, x_old_to_new, y_old_to_new) for t in tiles]
    return new_tiles, x_old_to_new, y_old_to_new, x_new_to_old, y_new_to_old

def transform_tile(tile, x_map, y_map):
    return [x_map[tile[0]], y_map[tile[1]]]

def is_intersecting(t1, t2, case):
    if t1[0] == t2[0]:
        if t1[0] == case[0] and max(t1[1], t2[1]) <= case[1]:
            return 1
        return 0
    if t1[1] < case[1]:
        if min(t1[0], t2[0]) < case[0] and max(t1[0], t2[0]) > case[0]:
            return 1
    return 0

def is_inside(x, y, tiles):
    n_intersects = 0
    for i in range(len(tiles)):
        j = (i + 1) % len(tiles)
        new_intersects = is_intersecting(tiles[i], tiles[j], [x, y]) 
        n_intersects += new_intersects
    if n_intersects % 2 == 1:
        return True
    return False

def is_crossing(a, b, t1, t2):
    if a[0] == b[0] and t1[0] == t2[0] or a[1] == b[1] and t1[1] == t2[1]:
        return False

    if t1[0] != t2[0]:
        max_x, max_y = max(t1[0], t2[0]), max(a[1], b[1])
        min_x, min_y = min(t1[0], t2[0]), min(a[1], b[1])
        return a[0] >= min_x and a[0] <= max_x and t1[1] >= min_y and t1[1] <= max_y
    else:
        max_x, max_y = max(a[0], b[0]), max(t1[1], t2[1])
        min_x, min_y = min(a[0], b[0]), min(t1[1], t2[1])
        return t1[0] >= min_x and t1[0] <= max_x and a[1] >= min_y and a[1] <= max_y

def get_corners(a, b):
    return [
        [min(a[0], b[0]) + 1, min(a[1], b[1]) + 1],
        [max(a[0], b[0]) - 1, min(a[1], b[1]) + 1],
        [min(a[0], b[0]) + 1, max(a[1], b[1]) - 1],
        [max(a[0], b[0]) - 1, max(a[1], b[1]) - 1],
    ]



def is_valid(t1, t2, tiles):
    for t in tiles:
        if t[0] > min(t1[0], t2[0]) and t[0] < max(t1[0], t2[0]) and t[1] > min(t1[1], t2[1]) and t[1] < max(t1[1], t2[1]):
            # print("invaliid: tile inside")
            return False

    for corner in get_corners(t1, t2):
        if not is_inside(corner[0], corner[1], tiles):
            # print("invaliid: corner outside", corner)
            return False

    for i in range(len(tiles)):
        j = (i + 1) % len(tiles)
        if is_crossing(t1, t2, tiles[j], tiles[i]):
            # print(t1, t2, "is crossing", tiles[j], tiles[i])
            if tiles[i][1] ==tiles[j][1]:
                y = tiles[j][1]
                ok = True
                if y != max(t1[1], t2[1]):
                    ok = ok and is_inside(t1[0], y + 1 , tiles)
                if y != min(t1[1], t2[1]):
                    ok = ok and is_inside(t1[0], y - 1 , tiles)
                if not ok:
                    # print("invaliid: crossed line is outside")
                    return False
            if tiles[i][0] ==tiles[j][0]:
                x = tiles[j][1]
                ok = True
                if x != max(t1[0], t2[0]):
                    ok = ok and is_inside(x + 1 , t1[1], tiles)
                if x != min(t1[0], t2[0]):
                    ok = ok and is_inside(x - 1 , t1[1], tiles)
                if not ok:
                    # print("invaliid: crossed line is outside")
                    return False

    return True

@printer
def part2():
    old_tiles = process_input()
    tiles, _, _, x_new_to_old, y_new_to_old = reduce_dims(old_tiles)
    print(tiles)
    mx = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            original_i = transform_tile(tiles[i], x_new_to_old, y_new_to_old)
            original_j = transform_tile(tiles[j], x_new_to_old, y_new_to_old)
            areer = area(original_i, original_j)
            if areer > mx and is_valid(tiles[i], tiles[j], tiles):
                mx = areer
                print(original_i, original_j)
    return mx



part2()
