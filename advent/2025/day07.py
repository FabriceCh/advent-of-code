from functools import cache
from advent.utils.utils import Grid, printer, read_file

ar = read_file("input")
# ar = [
#     ".......S.......",
#     "...............",
#     ".......^.......",
#     "...............",
#     "......^.^......",
#     "...............",
#     ".....^.^.^.....",
#     "...............",
#     "....^.^...^....",
#     "...............",
#     "...^.^...^.^...",
#     "...............",
#     "..^...^.....^..",
#     "...............",
#     ".^.^.^.^.^...^.",
#     "...............",
# ]


@printer
def part1():
    total = [0]
    grid = Grid(ar)
    start = (0, 0)
    for v, x, y in grid:
        if v == "S":
            start = (x, y)
            break

    def beam(grid: Grid, x, y, total):
        bottom = grid.get_south_coord(x, y)
        # print(bottom)
        # print(grid)
        if grid.is_out_of_bounds(*bottom):
            return
        bot_val = grid.get(*bottom)
        if bot_val == ".":
            grid.set(*bottom, "|")
            beam(grid, *bottom, total)
        elif bot_val == "^":
            left, right = grid.get_west_coord(*bottom), grid.get_east_coord(*bottom)
            grid.set(*left, "|")
            grid.set(*right, "|")
            beam(grid, *left, total)
            beam(grid, *right, total)
            total[0] += 1
    beam(grid, *start, total)
    return total



# part1()

@printer
def part2():
    total = [0]
    grid = Grid(ar)
    start = (0, 0)
    for v, x, y in grid:
        if v == "S":
            start = (x, y)
            break

    @cache
    def beam(grid: Grid, x, y) -> int:
        bottom = grid.get_south_coord(x, y)
        # print(bottom)
        # print(grid)
        if grid.is_out_of_bounds(*bottom):
            return 1
        bot_val = grid.get(*bottom)
        if bot_val == "." or bot_val == "|":
            grid.set(*bottom, "|")
            return beam(grid, *bottom)
        elif bot_val == "^":
            left, right = grid.get_west_coord(*bottom), grid.get_east_coord(*bottom)
            grid.set(*left, "|")
            grid.set(*right, "|")
            tot = beam(grid, *left)
            tot += beam(grid, *right)
            return tot
    return beam(grid, *start)

part2()

