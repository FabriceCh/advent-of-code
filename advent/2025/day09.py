from functools import cache
from types import new_class
from advent.utils.utils import printer, read_file
from PIL import Image
import numpy as np

ar = read_file("input")

TESTING = False
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
    return (abs(t1[1] - t2[1]) + 1) * (abs(t1[0] - t2[0]) + 1)

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
    # ON the line check first
    if t1[0] == t2[0]:
        if min(t1[1], t2[1]) <= case[1] and case[1] >= max(t1[1], t2[1]) and case[0] == t1[0]:
            return 2 # ON the line
        else:
            return 0
    else:
        if min(t1[0], t2[0]) <= case[0] and case[0] >= max(t1[0], t2[0]) and case[1] == t1[1]:
            return 2 # ON the line

    if t1[1] < case[1]:
        if min(t1[0], t2[0]) <= case[0] and max(t1[0], t2[0]) >= case[0]:
            return 1
    return 0

def is_inside(x, y, tiles):
    # print("is", x, y, "inside")
    if [x, y] in tiles:
        return True
    n_intersects = 0
    for i in range(len(tiles)):
        j = (i + 1) % len(tiles)
        new_intersects = is_intersecting(tiles[i], tiles[j], [x, y]) 
        if new_intersects == 2: # ON a line
            return True
        n_intersects += new_intersects
    if n_intersects % 2 == 1:
        return True
    return False

def is_crossing(a, b, t1, t2):
    if a[0] == b[0] and t1[0] == t2[0] or a[1] == b[1] and t1[1] == t2[1]:
        return False

    if t1 in [a, b] or t2 in [a,b]:
        return False

    if t1[0] != t2[0]:
        max_x, max_y = max(t1[0], t2[0]), max(a[1], b[1])
        min_x, min_y = min(t1[0], t2[0]), min(a[1], b[1])
        return a[0] > min_x and a[0] < max_x and t1[1] > min_y and t1[1] < max_y
    else:
        max_x, max_y = max(a[0], b[0]), max(t1[1], t2[1])
        min_x, min_y = min(a[0], b[0]), min(t1[1], t2[1])
        return t1[0] > min_x and t1[0] < max_x and a[1] > min_y and a[1] < max_y

def get_corners(t1, t2):
    maxx, minx, maxy, miny = max(t1[0], t2[0]), min(t1[0], t2[0]),max(t1[1], t2[1]), min(t1[1], t2[1])
    return [
        [maxx - 1, maxy],
        [minx + 1, maxy],
        [maxx - 1, miny],
        [minx + 1, miny],
        [maxx, miny + 1 ],
        [minx, miny + 1 ],
        [maxx, maxy - 1 ],
        [minx, maxy - 1 ],
    ]


def is_valid(t1, t2, tiles):
    for t in tiles:
        if t[0] > min(t1[0], t2[0]) and t[0] < max(t1[0], t2[0]) and t[1] > min(t1[1], t2[1]) and t[1] < max(t1[1], t2[1]):
            print(f"invalid: tile {t} inside {t1} {t2}")
            return False

    for c in get_corners(t1, t2):
        if not is_inside(c[0], c[1], tiles):
            return False

    for i in range(len(tiles)):
        j = (i + 1) % len(tiles)
        if is_crossing(t1, t2, tiles[j], tiles[i]):
            return False
            # print(t1, t2, "is crossing", tiles[j], tiles[i])
            # if tiles[i][1] == tiles[j][1]:
            #     y = tiles[j][1]
            #     if y != max(t1[1], t2[1]):
            #         if not is_inside(t1[0], y + 1 , tiles):
            #             return False
            #     if y != min(t1[1], t2[1]):
            #         if not is_inside(t1[0], y - 1 , tiles):
            #             return False
            # if tiles[i][0] == tiles[j][0]:
            #     x = tiles[j][0]
            #     if x != max(t1[0], t2[0]):
            #         if not is_inside(x + 1 , t1[1], tiles):
            #             return False
            #     if x != min(t1[0], t2[0]):
            #         if not is_inside(x - 1 , t1[1], tiles):
            #             return False

    return True

@printer
def part2():
    old_tiles = process_input()
    tiles, xon, yon, x_new_to_old, y_new_to_old = reduce_dims(old_tiles)
    # mx = 0
    # aaa = []
    # for i in range(len(tiles)):
    #     for j in range(i + 1, len(tiles)):
    #         original_i = transform_tile(tiles[i], x_new_to_old, y_new_to_old)
    #         original_j = transform_tile(tiles[j], x_new_to_old, y_new_to_old)
    #         ti, tj = tiles[i], tiles[j]
    #         # print(ti, tj)
    #         # areer = area(ti, tj)
    #         areer = area(original_i, original_j)
    #         if areer > mx and is_valid(ti, tj, tiles):
    #             mx = areer
    #             aaa = [ti, tj]
    #             print(original_i, original_j)
    # # return mx
    # # return is_valid([2,0], [0,5], tiles)

    # size_x = max(list((x_new_to_old.keys())))
    # size_y = max(list((y_new_to_old.keys())))
    # array_data = np.zeros((size_x + 1, size_y + 1, 3), dtype=np.uint8)
    # for i in range(len(tiles)):
    #     t1 = tiles[i]
    #     t2 = tiles[(i + 1) % len(tiles)]
    #     if t1[0] != t2[0]:
    #         max_x = max(t1[0], t2[0])
    #         min_x = min(t1[0], t2[0])
    #         for a in range(min_x, max_x):
    #             array_data[a][t1[1]] = [0, 0, 255]
    #     else:
    #         max_y = max(t1[1], t2[1])
    #         min_y = min(t1[1], t2[1])
    #         for a in range(min_y, max_y):
    #             array_data[t1[0]][a] = [0, 0, 255]
    # t1, t2 = aaa
    # max_x, max_y = max(t1[0], t2[0]), max(t1[1], t2[1])
    # min_x, min_y = min(t1[0], t2[0]), min(t1[1], t2[1])

    # for i in range(min_x, max_x):
    #     array_data[i][min_y] = [255, 0, 0]
    #     array_data[i][max_y] = [255, 0, 0]
    # for i in range(min_y, max_y + 1):
    #     array_data[max_x][i] = [255, 0, 0]
    #     array_data[min_x][i] = [255, 0, 0]

    # max_x, max_y = xon[94584], yon[67490] 
    # min_x, min_y = xon[5790], yon[50147]
    # for i in range(min_x, max_x):
    #     array_data[i][min_y] = [0, 255, 0]
    #     array_data[i][max_y] = [0, 255, 0]
    # for i in range(min_y, max_y + 1):
    #     array_data[max_x][i] = [0, 255, 0]
    #     array_data[min_x][i] = [0, 255, 0]

    # array_data[216][122] = [255, 255, 255]
    # image = Image.fromarray(array_data, "RGB")
    # if not TESTING:
    #     image = image.resize(( 1000, 1000 ), Image.Resampling.LANCZOS)
    # image.save("day9.bmp")
    # print("image saved")
    # return mx

    a1 = [5790, 67490]
    a2 = [94584, 50147]
    n1 = [xon[a1[0]], yon[a1[1]]]
    n2 = [xon[a2[0]], yon[a2[1]]]
    # print(is_valid(n1, n2, tiles))
    print(is_inside(31, 122, tiles))





part2()



