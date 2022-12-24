from utils import read_file
from typing import List
from enum import Enum
import numpy as np


lines = read_file("/home/fabrice/advent-of-code/2022/input")

lines2 = [
    "        ...#    ", #        1111    
    "        .#..    ", #        1111    
    "        #...    ", #        1111    
    "        ....    ", #        1111    
    "...#.......#    ", #222233334444    
    "........#...    ", #222233334444    
    "..#....#....    ", #222233334444    
    "..........#.    ", #222233334444    
    "        ...#....", #        55556666
    "        .....#..", #        55556666
    "        .#......", #        55556666
    "        ......#.", #        55556666
    "",
    "10R5L5R10L4R5L5",

]

class Dir(Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

class Rotator:
    def __init__(self):
        self.current_dir_index = 0
        self.ordering = [Dir.RIGHT, Dir.DOWN, Dir.LEFT, Dir.UP]
    def rotate(self, letter):
        if letter == "R":
            self.current_dir_index += 1
        elif letter == "L":
            self.current_dir_index += 3
        self.current_dir_index = self.current_dir_index % len(self.ordering)
    def get_current_dir(self):
        return self.ordering[self.current_dir_index]


class Face:
    def __init__(self):
        self.map = []
        self.upper_face = None
        self.downward_face = None
        self.right_face = None
        self.left_face = None
        self.id = 1
    
    def add_row(self, row):
        if len(self.map) == 0:
            self.map.append(list(row))
        else:
            self.map.append(list(row))

    def get_size(self):
        return len(self.map)

    def get_el_at_pos(self, pos):
        return self.map[pos[0]][pos[1]]

    def __repr__(self):
        string = ""
        for r in self.map:
            string += "".join(r) + "\n"
        return string


def get_new_pos(pos: List, dir: Dir):
    if dir == Dir.UP:
        new_pos = (pos[0] - 1, pos[1])
    if dir == Dir.DOWN:
        new_pos = (pos[0] + 1, pos[1])
    if dir == Dir.LEFT:
        new_pos = (pos[0], pos[1] - 1)
    if dir == Dir.RIGHT:
        new_pos = (pos[0], pos[1] + 1)
    return new_pos


def get_real_new_pos(pos, dir: Dir, face: Face):
    def  update_face(face, new_face):
        if new_face is not None:
            return new_face
        else:
            return face
    temp_new_pos = get_new_pos(pos, dir)
    maxv = face.get_size() - 1
    vert = temp_new_pos[0]
    hori = temp_new_pos[1]
    new_face = face
    if vert > maxv: # too down
        vert = 0
        new_face = update_face(face, face.downward_face)
    if vert < 0: # too up
        vert = maxv
        new_face = update_face(face, face.upper_face)
    if hori > maxv: # too right
        hori = 0
        new_face = update_face(face, face.right_face)
    if hori < 0: # too left
        hori = maxv
        new_face = update_face(face, face.left_face)
    return (vert, hori), new_face



def get_faces(ar):
    min_row_len = np.inf
    for row in ar:
        if row != "" and row != ar[-1]:
            if len(row.replace(" ", "")) < min_row_len:
                min_row_len = len(row.replace(" ", ""))
    cube_dim = min_row_len
    faces: List[Face] = []
    prev_n_faces = 0
    for row in ar:
        if row == "" or row == ar[-1]:
            continue
        r = list(row.replace(" ", ""))
        n_faces = len(r) // cube_dim
        if n_faces != prev_n_faces:
            faces += [Face() for _ in range(n_faces)]
        faces_rows = list(np.array_split(r, n_faces))
        for i, single_row in enumerate(faces_rows):
            faces[-(n_faces - i)].add_row(single_row)
        prev_n_faces = n_faces
    return faces

def get_input_directions(ar):
    dirss = ar[-1]
    #dirss = "2R1L99R5L99L5R11L5R99R1L99R1L99L1R99R1L5R6R99L1R2L2R2L2R2L1L11R99L5L1L5R1R5L3R2L33R7R4L"
    in_dirs = []
    distances = []
    cur = ""
    for i, el in enumerate(dirss):
        if el in ["L", "R"]:
            in_dirs.append(el)
        else:
            cur += el
            if i + 1 < len(dirss) and dirss[i + 1] in ["L", "R"]:
                distances.append(int(cur))
                cur = ""

    return in_dirs, distances + [int("".join(dirss[-2:]))]

def arrange_faces_SAMPLE_TEST(faces: List[Face]):
    faces[0].downward_face = faces[3]
    faces[0].upper_face = faces[5]

    faces[1].left_face = faces[3]
    faces[1].right_face = faces[2]

    faces[2].left_face = faces[1]
    faces[2].right_face = faces[3]

    faces[3].left_face = faces[2]
    faces[3].right_face = faces[1]
    faces[3].upper_face = faces[0]
    faces[3].downward_face = faces[4]

    faces[4].left_face = faces[5]
    faces[4].right_face = faces[5]
    faces[4].upper_face = faces[3]
    faces[4].downward_face = faces[0]

    faces[5].right_face = faces[4]
    faces[5].left_face = faces[4]

    faces[0].id = 1
    faces[1].id = 2
    faces[2].id = 3
    faces[3].id = 4
    faces[4].id = 5
    faces[5].id = 6

def arrange_faces(faces: List[Face]):
    faces[0].left_face = faces[1]
    faces[0].right_face = faces[1]
    faces[0].upper_face = faces[4]
    faces[0].downward_face = faces[2]

    faces[1].left_face = faces[0]
    faces[1].right_face = faces[0]

    faces[2].upper_face = faces[0]
    faces[2].downward_face = faces[4]

    faces[3].left_face = faces[4]
    faces[3].right_face = faces[4]
    faces[3].upper_face = faces[5]
    faces[3].downward_face = faces[5]

    faces[4].left_face = faces[3]
    faces[4].right_face = faces[3]
    faces[4].upper_face = faces[2]
    faces[4].downward_face = faces[0]

    faces[5].upper_face = faces[3]
    faces[5].downward_face = faces[3]

    faces[0].id = 1
    faces[1].id = 2
    faces[2].id = 3
    faces[3].id = 4
    faces[4].id = 5
    faces[5].id = 6


def part1_adjust_final_posSAMPLE_INPUT(pos, face: Face):
    def get_offs(n):
        return 1 + n*face.get_size()
    if face.id == 1:
        return (pos[0] + get_offs(0), pos[1] + get_offs(2))
    if face.id == 2:
        return (pos[0] + get_offs(1), pos[1] + get_offs(0))
    if face.id == 3:
        return (pos[0] + get_offs(1), pos[1] + get_offs(1))
    if face.id == 4:
        return (pos[0] + get_offs(1), pos[1] + get_offs(2))
    if face.id == 5:
        return (pos[0] + get_offs(2), pos[1] + get_offs(2))
    if face.id == 6:
        return (pos[0] + get_offs(2), pos[1] + get_offs(3))

def part1_adjust_final_pos(pos, face: Face):
    def get_offs(n):
        return 1 + n*face.get_size()
    if face.id == 1:
        return (pos[0] + get_offs(0), pos[1] + get_offs(1))
    if face.id == 2:
        return (pos[0] + get_offs(0), pos[1] + get_offs(2))
    if face.id == 3:
        return (pos[0] + get_offs(1), pos[1] + get_offs(1))
    if face.id == 4:
        return (pos[0] + get_offs(2), pos[1] + get_offs(0))
    if face.id == 5:
        return (pos[0] + get_offs(2), pos[1] + get_offs(1))
    if face.id == 6:
        return (pos[0] + get_offs(3), pos[1] + get_offs(0))


def log_path(f, p, d):
    if d == Dir.UP:
        f.map[p[0]][p[1]] = "^"
    if d == Dir.DOWN:
        f.map[p[0]][p[1]] = "v"
    if d == Dir.LEFT:
        f.map[p[0]][p[1]] = "<"
    if d == Dir.RIGHT:
        f.map[p[0]][p[1]] = ">"

def part1():
    faces = get_faces(lines)
    input_dirs, distances = get_input_directions(lines)
    
    rotator = Rotator()
    arrange_faces(faces)
    current_face = faces[0]
    # currentpos = j, i (row, line)
    current_pos = [0, 0]
    print(len(input_dirs), len(distances))


    for cur_dd_index, cur_dist in enumerate(distances):
        for _ in range(cur_dist):
            #current_face.map[current_pos[0]][current_pos[1]] = "x"
            log_path(current_face, current_pos, rotator.get_current_dir())
            next_pos, next_face = get_real_new_pos(current_pos, rotator.get_current_dir(), current_face)
            if next_face.get_el_at_pos(next_pos) == "#":
                break
            else:
                current_face, current_pos = next_face, next_pos
            log_path(current_face, current_pos, rotator.get_current_dir())
        if cur_dd_index < len(input_dirs):
            cur_in_dir = input_dirs[cur_dd_index]
            rotator.rotate(cur_in_dir)
    current_pos = part1_adjust_final_pos(current_pos, current_face)
    
    for f in faces:
        print(f.id)
        print(f)
    
    print((1000 * current_pos[0]) + (4 * current_pos[1]) + rotator.get_current_dir().value)
    print(rotator.get_current_dir())

part1()
