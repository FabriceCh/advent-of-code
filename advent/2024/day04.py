from utils import read_file, Grid

ar = read_file("2024/input")
# ar = [
#     "MMMSXXMASM",
#     "MSAMXMSMSA",
#     "AMXSXMAAMM",
#     "MSAMASMSMX",
#     "XMASAMXAMM",
#     "XXAMMXXAMA",
#     "SMSMSASXSS",
#     "SAXAMASAAA",
#     "MAMMMXMMMM",
#     "MXMXAXMASX",
# ]

# part 1
# iterate over each row and each char, if it's an X, verify all directions for XMAS
ar = [[char for char in string] for string in ar]
grid = Grid(ar)
count = 0
for letter, x, y in grid:
    if letter == "X":
        for direction_search in grid.list_get_coordinates_functions():
            next_n = grid.get_next_n(x, y, direction_search, 3)
            if "".join(next_n) == "MAS":
                count += 1

print(count)

# part 2
count = 0
for letter, x, y in grid:
    if letter == "A":
        try:
            nw, ne, sw, se = (
                grid.get(*grid.get_north_west_coord(x, y)),
                grid.get(*grid.get_north_east_coord(x, y)),
                grid.get(*grid.get_south_west_coord(x, y)),
                grid.get(*grid.get_south_east_coord(x, y)),
            )
        except IndexError:
            continue
        if ((nw == "S" and se == "M") or (nw == "M" and se == "S")) and (
            (ne == "S" and sw == "M") or (ne == "M" and sw == "S")
        ):
            count += 1

print(count)
