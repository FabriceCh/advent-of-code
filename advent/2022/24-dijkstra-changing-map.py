from typing import List
from utils import read_file

lines = read_file("/home/fabrice/advent-of-code/2022/input")

lines3 = [
    "#.######",
    "#>>.<^<#",
    "#.<..<<#",
    "#>v.><>#",
    "#<^v^^>#",
    "######.#",

]

ar = [list(l) for l in lines]
for l in lines:
    print(l)
MAP_SIZE_VERT = len(ar)
MAP_SIZE_HORI = len(ar[0])


class Storm:
    def __init__(self, pos, dir):
        self.pos = pos
        self.dir = dir
    def incr(self):
        if self.dir == ">":
            self.pos = (self.pos[0], self.pos[1] + 1)
        elif self.dir == "<":
            self.pos = (self.pos[0], self.pos[1] - 1)
        elif self.dir == "^":
            self.pos = (self.pos[0] - 1, self.pos[1])
        elif self.dir == "v":
            self.pos = (self.pos[0] + 1, self.pos[1])

        if self.pos[0] == MAP_SIZE_VERT - 1:
            self.pos = ((self.pos[0] % (MAP_SIZE_VERT - 1)) + 1, self.pos[1])
        elif self.pos[1] == MAP_SIZE_HORI - 1:
            self.pos = (self.pos[0], (self.pos[1] % (MAP_SIZE_HORI - 1)) + 1)
        elif self.pos[0] == 0:
            self.pos = (MAP_SIZE_VERT - 2, self.pos[1])
        elif self.pos[1] == 0:
            self.pos = (self.pos[0], MAP_SIZE_HORI - 2)
        

def get_storms(ar) -> List[Storm]:
    storms: List[Storm] = []
    for i, l in enumerate(ar):
        for j, el in enumerate(l):
            if el in [">", "<", "v", "^"]:
                storms.append(Storm((i, j), el))
    return storms

def get_adjs(cur_pos, storms, ar):
    storms_pos = [s.pos for s in storms]
    adjs = [cur_pos]
    if cur_pos[0] - 1 >= 0:
        adjs.append((cur_pos[0] - 1, cur_pos[1]))
    if cur_pos[0] + 1 < MAP_SIZE_VERT:
        adjs.append((cur_pos[0] + 1, cur_pos[1]))
    adjs.append((cur_pos[0], cur_pos[1] + 1))
    adjs.append((cur_pos[0], cur_pos[1] - 1))

    legit_pos = []
    for pp in adjs:
        if pp not in storms_pos and ar[pp[0]][pp[1]] != "#":
            legit_pos.append(pp)

    return legit_pos

def part1():
    storms = get_storms(ar)
    start = (0,1)
    end = (MAP_SIZE_VERT - 1, MAP_SIZE_HORI - 2)
    current_possible_pos = {start}
    counter = 0
    while end not in current_possible_pos:
        # incr turn counter
        counter += 1
        # storms all move once
        for s in storms:
            s.incr()
        # gather every new possible positions
        next_pos = set()
        for cur_pos in current_possible_pos:
            adjs = get_adjs(cur_pos, storms, ar)
            for a in adjs:
                next_pos.add(a)
        current_possible_pos = next_pos
    print(counter)
        

def part2():
    storms = get_storms(ar)
    start = (0,1)
    end = (MAP_SIZE_VERT - 1, MAP_SIZE_HORI - 2)
    # go to end
    current_possible_pos = {start}
    counter = 0
    while end not in current_possible_pos:
        # incr turn counter
        counter += 1
        # storms all move once
        for s in storms:
            s.incr()
        # gather every new possible positions
        next_pos = set()
        for cur_pos in current_possible_pos:
            adjs = get_adjs(cur_pos, storms, ar)
            for a in adjs:
                next_pos.add(a)
        current_possible_pos = next_pos
    #print(counter)
    # go back to start
    current_possible_pos = {end}
    while start not in current_possible_pos:
        # incr turn counter
        counter += 1
        # storms all move once
        for s in storms:
            s.incr()
        # gather every new possible positions
        next_pos = set()
        for cur_pos in current_possible_pos:
            adjs = get_adjs(cur_pos, storms, ar)
            for a in adjs:
                next_pos.add(a)
        current_possible_pos = next_pos

    # go back to end
    current_possible_pos = {start}
    while end not in current_possible_pos:
        # incr turn counter
        counter += 1
        # storms all move once
        for s in storms:
            s.incr()
        # gather every new possible positions
        next_pos = set()
        for cur_pos in current_possible_pos:
            adjs = get_adjs(cur_pos, storms, ar)
            for a in adjs:
                next_pos.add(a)
        current_possible_pos = next_pos
    print(counter)

part2()
