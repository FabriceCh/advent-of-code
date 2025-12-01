from advent.utils.utils import Grid, read_file

ar = read_file()

# ar = [
#     "##########",
#     "#..O..O.O#",
#     "#......O.#",
#     "#.OO..O.O#",
#     "#..O@..O.#",
#     "#O#..O...#",
#     "#O..O..O.#",
#     "#.OO.O.OO#",
#     "#....O...#",
#     "##########",
#     "",
#     "<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^",
#     "vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v",
#     "><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<",
#     "<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^",
#     "^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><",
#     "^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^",
#     ">^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^",
#     "<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>",
#     "^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>",
#     "v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^",
# ]

# ar = [
#     "#######",
#     "#...#.#",
#     "#.....#",
#     "#..OO@#",
#     "#..O..#",
#     "#.....#",
#     "#######",
#     "",
#     "<vv<<^^<<^^",
# ]

grid_lines = []
instructions = []
grid_mode = True
for line in ar:
    if line == "":
        grid_mode = False
        continue
    if grid_mode:
        grid_lines.append(line)
    else:
        instructions.append(line)

instructions = "".join(instructions)

grid = Grid(grid_lines)


def get_current_pos(grid):
    current_pos = (0, 0)
    for val, x, y in grid:
        if val == "@":
            current_pos = (x, y)
    return current_pos


def execute_instruction(ins, grid, current_pos):
    direction_fun = grid.get_direction_coord_fun(ins)
    next_n_items = grid.get_next_n(*current_pos, direction_fun, None, True)

    for i, item in enumerate(next_n_items):
        if item == ".":
            grid.shift_next_n(*current_pos, direction_fun, i, True)
            current_pos = direction_fun(*current_pos)
            break
        elif item == "#":
            break
        else:
            continue
    return current_pos


current_pos = get_current_pos(grid)
# print(grid)
for ins in instructions:
    current_pos = execute_instruction(ins, grid, current_pos)
    # print(ins)
    # print(grid)
total = 0
for val, x, y in grid:
    if val == "O":
        total += (100 * y) + x

print(total)

# part2


def validate_grid(g: Grid):
    for value, x, y in g:
        if value == "[":
            if g.get(x + 1, y) != "]":
                print("BIG PROBLEM")
                print(grid)
                return False
    return True


new_grid_array = []
for line in grid_lines:
    new_line = ""
    for item in line:
        if item == "#":
            new_line += "##"
        if item == ".":
            new_line += ".."
        if item == "O":
            new_line += "[]"
        if item == "@":
            new_line += "@."
    new_grid_array.append(new_line)

grid = Grid(new_grid_array)


def upper_pos(pos):
    return (pos[0], pos[1] - 1)


def lower_pos(pos):
    return (pos[0], pos[1] + 1)


def find_boxes(box_pos, boxes, up=True):
    if grid.get(*box_pos) == "[":
        other_box_pos = (box_pos[0] + 1, box_pos[1])
        boxes += [box_pos, other_box_pos]
        if up:
            return find_boxes(upper_pos(box_pos), boxes, up) and find_boxes(
                upper_pos(other_box_pos), boxes, up
            )
        else:
            return find_boxes(lower_pos(box_pos), boxes, up) and find_boxes(
                lower_pos(other_box_pos), boxes, up
            )
    elif grid.get(*box_pos) == "]":
        other_box_pos = (box_pos[0] - 1, box_pos[1])
        boxes += [box_pos, other_box_pos]
        if up:
            return find_boxes(upper_pos(box_pos), boxes, up) and find_boxes(
                upper_pos(other_box_pos), boxes, up
            )
        else:
            return find_boxes(lower_pos(box_pos), boxes, up) and find_boxes(
                lower_pos(other_box_pos), boxes, up
            )
    elif grid.get(*box_pos) == "#":
        return False
    else:
        return True


def move_boxes(boxes: list[tuple[int, int]], up):
    boxes = list(set(boxes))

    def move(xx, yy, up):
        if up:
            grid.set(xx, yy - 1, grid.get(xx, yy))
            grid.set(xx, yy, ".")
        else:
            grid.set(xx, yy + 1, grid.get(xx, yy))
            grid.set(xx, yy, ".")

    if up:
        boxes.sort(key=lambda item: item[1], reverse=False)
    else:
        boxes.sort(key=lambda item: item[1], reverse=True)

    for box in boxes:
        move(*box, up)
        # print(grid)


def execute_up_down(grid: Grid, current_pos: tuple[int, int], up):
    if up:
        box_pos = upper_pos(current_pos)
    else:
        box_pos = lower_pos(current_pos)

    boxes = []
    found_boxes = find_boxes(box_pos, boxes, up)
    if found_boxes:
        if boxes:
            # print("boxes found and able to move")
            move_boxes(boxes, up)
            if up:
                grid.shift_next_n(*current_pos, grid.get_north_coord, 1, True)
                current_pos = upper_pos(current_pos)
            else:
                grid.shift_next_n(*current_pos, grid.get_south_coord, 1, True)
                current_pos = lower_pos(current_pos)
        else:
            if up:
                ins = "^"
            else:
                ins = "v"
            current_pos = execute_instruction(ins, grid, current_pos)
    return current_pos


current_pos = get_current_pos(grid)
# print(grid)

for ins in instructions:
    # print(ins)
    # print(grid)
    # print()
    if ins in ["<", ">"]:
        current_pos = execute_instruction(ins, grid, current_pos)
    elif ins == "^":
        current_pos = execute_up_down(grid, current_pos, up=True)
    else:
        current_pos = execute_up_down(grid, current_pos, up=False)
    # if not validate_grid(grid):
    #     print(ins)
    #     break
    # print(grid)
    # print("------------")


# print(grid)

total = 0
for val, x, y in grid:
    if val == "[":
        total += (100 * y) + x

print(total)
