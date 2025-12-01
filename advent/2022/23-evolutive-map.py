import copy
import numpy as np
from utils import read_file

lines = read_file("/home/fabrice/advent-of-code/2022/input")
lines2 = [
    "..............",
    "..............",
    ".......#......",
    ".....###.#....",
    "...#...#.#....",
    "....#...##....",
    "...#.###......",
    "...##.#.##....",
    "....#..#......",
    "..............",
    "..............",
    "..............",
]

def lines_to_pos(lines):
    pos = []
    for i, l in enumerate(lines):
        for j, el in enumerate(l):
            if el == "#":
                pos.append((i, j))
    return pos

class Directioner:
    global_idx = 0

    def __init__(self):
        self._directions = ["N", "S", "W", "E"]
        self.current_idx = Directioner.global_idx
        self.n_called = 0

    def get_current_dir(self):
        return self._directions[self.current_idx]

    def increment_dir(self):
        if self.n_called < len(self._directions):
            self.current_idx = (self.current_idx + 1) % len(self._directions)
            self.n_called += 1
            return True
        else:
            return False

    def global_incr_dir(self):
        Directioner.global_idx = (Directioner.global_idx + 1) % len(self._directions)

def get_neighs_pos(pos, direction):
    if direction == "N":
        return [
            (pos[0] - 1, pos[1] - 1),
            (pos[0] - 1, pos[1]),
            (pos[0] - 1, pos[1] + 1),
        ]
    if direction == "E":
        return [
            (pos[0] - 1, pos[1] + 1),
            (pos[0]    , pos[1] + 1),
            (pos[0] + 1, pos[1] + 1),
        ]
    if direction == "S":
        return [
            (pos[0] + 1, pos[1] - 1),
            (pos[0] + 1, pos[1]),
            (pos[0] + 1, pos[1] + 1),
        ]
    if direction == "W":
        return [
            (pos[0] - 1, pos[1] - 1),
            (pos[0]    , pos[1] - 1),
            (pos[0] + 1, pos[1] - 1),
        ]

def get_all_neighs(pos):
    return [
        (pos[0] - 1, pos[1] - 1),
        (pos[0]    , pos[1] - 1),
        (pos[0] + 1, pos[1] - 1),

        (pos[0] - 1, pos[1]    ),
        (pos[0] + 1, pos[1]    ),

        (pos[0] + 1, pos[1] + 1),
        (pos[0] - 1, pos[1] + 1),
        (pos[0]    , pos[1] + 1),
    ]

def is_alone(p, all_pos):
    neighs = get_all_neighs(p)
    for n in neighs:
        if n in all_pos:
            return False
    return True

def is_over(all_pos):
    for p in all_pos:
        neighs = get_all_neighs(p)
        for n in neighs:
            if n in all_pos:
                return False
    return True


def count_dots(all_pos):
    min_i, max_i, min_j, max_j = np.inf, 0, np.inf, 0
    for p in all_pos:
        min_i = min(min_i, p[0])
        min_j = min(min_j, p[1])
        max_i = max(max_i, p[0])
        max_j = max(max_j, p[1])
    #print("min_i", min_i, "min_j", min_j, "max_i", max_i, "max_j", max_j)
    return ((max_i - min_i + 1) * (max_j - min_j + 1)) - len(all_pos)

def part1():
    main_dirrer = Directioner()
    all_pos = lines_to_pos(lines)
    for i in range(1000):
        #print("positions at start of", i, ":", all_pos)
        print(i)
        if is_over(all_pos):
            print("PART2 is over at:", i + 1)
            break
        # first phase: propose moves
        proposed_moves = [None for _ in range(len(all_pos))]
        for p_idx, p in enumerate(all_pos):
            # if already alone, don't move
            if is_alone(p, all_pos):
                continue
            # try all dirs in order, set proposed move if possible
            local_dirrer = Directioner()
            for _ in range(4):
                dir = local_dirrer.get_current_dir()
                neighs = get_neighs_pos(p, dir)
                is_dir_ok = True
                for n in neighs:
                    if n in all_pos:
                        is_dir_ok = False
                        break
                if is_dir_ok:
                    #print(dir, p, neighs[1])
                    proposed_moves[p_idx] = tuple(neighs[1])
                    break
                else:
                    local_dirrer.increment_dir()
        #print(proposed_moves)
        # second phase
        val_n_i = {}
        for i, prop in enumerate(proposed_moves):
            if prop not in val_n_i.keys():
                val_n_i[prop] = [i]
            else:
                val_n_i[prop].append(i)
        for poss, indexes in val_n_i.items():
            if poss is not None and len(indexes) > 1:
                for idx in indexes:
                    proposed_moves[idx] = None
        #print(proposed_moves, val_n_i)
        for i, move_pos in enumerate(proposed_moves):
            if move_pos is not None:
                all_pos[i] = move_pos

        main_dirrer.global_incr_dir()
    # part1
    #print(count_dots(all_pos))


part1()