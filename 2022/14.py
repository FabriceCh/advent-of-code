import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)
lines = []

file = open("/home/rprcz974/workspace/AOC/2022/input", "r")
for l in file.readlines():
    lines.append(l.rstrip())

lines2 = [
    "498,4 -> 498,6 -> 496,6",
    "503,4 -> 502,4 -> 502,9 -> 494,9",
]

rock_lines = []
all_rocks = []

for line in lines:
    positions = line.split(" -> ")
    positions = [pos.split(",") for pos in positions]
    positions = [[int(p[0]), int(p[1])] for p in positions]
    rock_lines.append(positions)
    all_rocks += positions

max_x, max_y = 0, 0
min_x, min_y = 1110, 1110
for p in all_rocks:
    if p[0] > max_x:
        max_x = p[0]

    if p[1] > max_y:
        max_y = p[1]
    
    if p[0] < min_x:
        min_x = p[0]
        
    if p[1] < min_y:
        min_y = p[1]

#print(max_x, max_y)
#print(min_x, min_y)
min_x -= 1

# consts
height = max_y + 2
largeur = 2 * height - 1
middle = height - 1
offset = 500 - middle

# reduce x to center
for l in rock_lines:
    for p in l:
        p[0] -= (offset)
#print(rock_lines)

# create grid

grid = [["." for i in range(largeur)] for i in range(height)]
grid = np.array(grid)
# fill grid with rocks
for line in rock_lines:
    rok1 = line.pop(0)
    while line:
        rok2 = line.pop(0)
        #print(rok1, rok2)
        if rok1[0] == rok2[0]:
            s, e = min(rok1[1], rok2[1]), max(rok1[1], rok2[1])
            grid[s:e+1, rok1[0]] = "#"
        else:
            s, e = min(rok1[0], rok2[0]), max(rok1[0], rok2[0])
            grid[rok2[1],s:e+1] = "#"
        rok1 = rok2
#grid[1:10,2] = "#"
#print(grid)

def fall(pp=None):
    #print(grid)
    if pp is None:
        pp = [0, middle]
    if grid[pp[0], pp[1]] == "o":
        return False
    #print(pp)
    if pp[0] == max_y + 1:
        grid[pp[0], pp[1]] = "o"
        return True
    if grid[pp[0] + 1, pp[1]] == ".":
        pp = [pp[0] + 1, pp[1]]
        return fall(pp)
    elif grid[pp[0] + 1, pp[1] - 1] == ".":
        pp = [pp[0] + 1, pp[1] - 1]
        return fall(pp)
    elif grid[pp[0] + 1, pp[1] + 1] == ".":
        pp = [pp[0] + 1, pp[1] + 1]
        return fall(pp)
    elif grid[pp[0] + 1, pp[1]] in ["#", "o"]:
        grid[pp[0], pp[1]] = "o"
        return True



def part1():
    c = 0
    while fall():
        c += 1
        #print(grid)
    print(c)

part1()
f = open("/home/rprcz974/workspace/AOC/2022/grid.txt", "w")
lines_to_w = [''.join([str(a) for a in l]) + "\n" for l in grid]
f.writelines(lines_to_w)
f.close()