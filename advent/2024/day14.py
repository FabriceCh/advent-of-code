import re
from advent.utils.utils import read_file, Grid


ar = read_file("input.txt")
# ar = [
#     "p=0,4 v=3,-3",
#     "p=6,3 v=-1,-3",
#     "p=10,3 v=-1,2",
#     "p=2,0 v=2,-1",
#     "p=0,0 v=1,3",
#     "p=3,0 v=-2,-2",
#     "p=7,6 v=-1,-3",
#     "p=3,0 v=-1,-2",
#     "p=9,3 v=2,3",
#     "p=7,3 v=-1,2",
#     "p=2,4 v=2,-3",
#     "p=9,5 v=-3,-3",
# ]

WIDTH = 101
HEIGHT = 103


class Robot:
    def __init__(self, start_x, start_y, vel_x, vel_y):
        self.start_x = start_x
        self.start_y = start_y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def compute_future(self, seconds):
        final_x = (self.start_x + self.vel_x * seconds) % WIDTH
        final_y = (self.start_y + self.vel_y * seconds) % HEIGHT
        return final_x, final_y


robots: list[Robot] = []
for line in ar:
    matches = re.findall(r"p\=([0-9]*,[0-9]*).*v\=(.*)", line)
    matches = matches[0]
    pos = [int(a) for a in matches[0].split(",")]
    vel = [int(a) for a in matches[1].split(",")]
    robots.append(Robot(*pos, *vel))

q1, q2, q3, q4 = 0, 0, 0, 0
for r in robots:
    x, y = r.compute_future(100)
    if x < WIDTH // 2 and y < HEIGHT // 2:
        q1 += 1
    if x < WIDTH // 2 and y > HEIGHT // 2:
        q3 += 1
    if x > WIDTH // 2 and y < HEIGHT // 2:
        q2 += 1
    if x > WIDTH // 2 and y > HEIGHT // 2:
        q4 += 1
print(q1 * q2 * q3 * q4)


# part 2
for i in range(0, 10000):
    grid = Grid([["." for _ in range(WIDTH)] for _ in range(HEIGHT)])
    for r in robots:
        x, y = r.compute_future(i)
        grid.set(x, y, "O")
    for line in grid._grid:
        if "OOOOOOOOOOO" in "".join(line):
            print(i)
            print(grid)
            print("------------------------------------------------------------")
            break
