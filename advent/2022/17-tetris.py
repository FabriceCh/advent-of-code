import numpy as np
import copy

lines = []

file = open("/home/rprcz974/workspace/AOC/2022/input", "r")
for l in file.readlines():
    lines.append(l.rstrip())

pattern = lines[0]
pattern2 = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
print("len of pattern:", len(pattern))


class RockGenerator:
    def __init__(self):
        self.rocks_order = ["minus", "plus", "Lshape", "line", "square"]
        self.current_rock_index = 0
        self.rocks_order = [np.where(np.array(self._rock_name_to_shape(a)) == "@") for a in self.rocks_order]

    def _rock_name_to_shape(self, name):
        if name not in self.rocks_order:
            raise Exception(f"{name} is not a rock")

        if name == "minus":
            return [["", "", "", "@", "@", "@", "@"]]
        elif name == "plus":
            return [
                ["", "", "", ".", "@", "."],
                ["", "", "", "@", "@", "@"],
                ["", "", "", ".", "@", "."]
            ]
        elif name == "Lshape":
            return [
                ["", "", "", ".", ".", "@"],
                ["", "", "", ".", ".", "@"],
                ["", "", "", "@", "@", "@"]
            ]
        elif name == "line":
            return [
                ["", "", "", "@"],
                ["", "", "", "@"],
                ["", "", "", "@"],
                ["", "", "", "@"] 
            ]
        elif name == "square":
            return [
                ["", "", "", "@", "@"],
                ["", "", "", "@", "@"]
            ]

    def get_next_rock(self):
        rock_index_to_return = self.current_rock_index
        self.current_rock_index += 1
        self.current_rock_index = self.current_rock_index % len(self.rocks_order)
        return copy.deepcopy(self.rocks_order[rock_index_to_return])

class DirGen:
    def __init__(self, pattern):
        self.pattern = pattern
        self.current_index = 0

    def get_next_dir(self):
        dir = self.pattern[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.pattern)
        return dir

class Tower:
    def __init__(self):
        self.dir_gen = DirGen(pattern=pattern)
        self.rock_gen = RockGenerator()
        self.grid = np.array([
            [True for i in range(9)]
        ])
        self.highest_point_height = 0
        self.grid_width = 7
        self.current_rock = None
        self.current_fall_count = None
        self.total_height = 0
        self.MAX_GRID_LEN = 1000
        self.REMOVABLE_LEN = 200
        self.journal = {}
        self.n_rocks = 0


    def process_state(self):
        
        key = (self.dir_gen.current_index, self.rock_gen.current_rock_index)
        value = self.n_rocks

        if key not in self.journal:
            self.journal[key] = {"raw": [value], "dif": []}
        else:
            self.journal[key]["raw"].append(value)
            self.journal[key]["dif"].append(value - self.journal[key]["raw"][-2])
            #if self.dir_gen.current_index < 4:
                #print(key, self.journal[key])

    def get_current_total_height(self):
        return self.total_height + self.highest_point_height

    def spawn_rock(self, rock):
        self.process_state()
        self.n_rocks += 1
        self.current_rock = list(rock)
        self.current_fall_count = 0
        empty_space = np.array([[True] + [False for i in range(7)] + [True] for _ in range(max(rock[0] + 1))])
        self.grid = np.concatenate((empty_space, self.grid), axis=0)


    def shift_rock(self):
        dir = self.dir_gen.get_next_dir()
        if dir == "<":
            shift_val = -1
        elif dir == ">":
            shift_val = 1
        can_shift = True

        for i, j in zip(self.current_rock[0], self.current_rock[1]):
            if self.grid[i][j + shift_val]:
                can_shift = False

        if can_shift:
            self.current_rock[1] += shift_val

    def fall_rock(self):
        if self.current_fall_count == 0:
            for i in range(3):
                self.shift_rock()
        self.shift_rock()
        can_fall = True
        for i, j in zip(self.current_rock[0], self.current_rock[1]):
            if self.grid[i + 1][j]:
                can_fall = False
        if can_fall:
            self.current_rock[0] += 1
            self.current_fall_count += 1
        else:
            self.grid[self.current_rock[0], self.current_rock[1]] = True
            self.highest_point_height = max(self.highest_point_height - self.current_fall_count + max(self.current_rock[0]) - min(self.current_rock[0]) + 1, self.highest_point_height)
            self.grid = self.grid[len(self.grid) - (self.highest_point_height + 1):, :]
            if len(self.grid) > self.MAX_GRID_LEN:
                self.grid = self.grid[:-self.REMOVABLE_LEN, :]
                self.total_height += self.REMOVABLE_LEN
                self.highest_point_height -= self.REMOVABLE_LEN
        return can_fall

tower = Tower()

ttt = 1000000000000

checks_inter = len(pattern) * 5
magic_number = 1695
jump_height = 2634
other_magic_number = ttt % magic_number
n_times = ttt // magic_number
print(other_magic_number, n_times)

first_pass = (5 * magic_number) + other_magic_number

for i in range(first_pass):
    next_rock = tower.rock_gen.get_next_rock()
    tower.spawn_rock(next_rock)
    while tower.fall_rock():
        continue

first_pass_height = tower.get_current_total_height()

answer = first_pass_height + ((n_times - 5) * jump_height)
print("answer:", answer)