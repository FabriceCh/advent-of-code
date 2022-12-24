from utils import read_file
import functools
from natsort import natsorted 
import copy
import json

ar = read_file("/home/fabrice/advent-of-code/2022/input")
ar2 = read_file("/home/fabrice/advent-of-code/2022/input_sample.txt")


pairs = []
cur_pair = []
for line in ar:
    if line != "":
        cur_pair.append(json.loads(line))
    else:
        pairs.append(copy.deepcopy(cur_pair))
        cur_pair = []

pairs2 = [
    [[],
    [3]]
]

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return "continue"
    elif isinstance(left, list) and isinstance(right, list):
        
        for i, el in enumerate(right):
            if i > len(left) - 1:
                return -1
            res = compare(left[i], el)
            if res == "continue":
                continue
            else:
                return res

        if len(right) > len(left):
            return -1
        elif len(right) < len(left):
            return 1
        else:
            return "continue"

    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])

def part1():
    c = 0
    for i, p in enumerate(pairs):
        #print("comparing", p[0], p[1])
        if compare(p[0], p[1]) == -1:
            #print(p)
            #print(i + 1)
            c += i + 1
        #if compare(p[0], p[1]) == "continue":
        #    print("WTF", p[0], p[1])
    print(c)

part1()


def part2(pairs):
    pairs = [p[0] for p in pairs] + [p[1] for p in pairs] + [[[2]], [[6]]]

    pairs.sort(key=functools.cmp_to_key(compare))
    


    print((pairs.index([[2]]) + 1) * (pairs.index([[6]]) + 1))
    #print(str_pairs)

part2(pairs)