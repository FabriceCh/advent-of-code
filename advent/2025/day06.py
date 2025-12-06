from advent.utils.utils import Grid, printer, read_file

ar = read_file("input")
# ar = [
# "123 328  51 64 ",
# " 45 64  387 23 ",
# "  6 98  215 31433",
# "*   +   *   +  ",
# ]


def part1():
    total = 0
    data = []
    for line in ar:
        data.append(line.split())

    for col in (zip(*data)):
        subtotal = 0
        for n in col[:-1]:
            if col[-1] == "+":
                subtotal += int(n)
            else:
                if subtotal == 0:
                    subtotal = 1
                subtotal *= int(n)
        total += subtotal

    return total

part1()


for line in ar:
    # print(len(line))
    while len(line) != 3713:
        line += " "
    # print(len(line))

@printer
def part2():
    total = 0

    grid = Grid(ar)
    cols = []
    maxlen = 0
    for l in ar:
        maxlen = max(maxlen, len(l))
    for i in range(maxlen):
        try:
            cols.append(grid.get_next_n(i, 0, grid.get_south_coord, include_start=True))
        except:
            c = []
            for line in ar:
                if i < len(line):
                    c.append(line[i])
            cols.append(c)
    for c in cols:
        print(c)

    sign = ""
    numbers = []
    i = 0
    for c in cols:
        i += 1
        cur_number = ""
        if c[-1] not in [" ", "*", "+"]:
            for d in c:
                cur_number += d
        else:
            for d in c[:-1]:
                    cur_number += d
        if cur_number.replace(" ", "") != "":
            numbers.append(int(cur_number))
        if cur_number.replace(" ", "") == "" or (i == len(cols)):
            if sign == "+":
                total += sum(numbers)
                # print()
                # print(numbers)
                # print(sum(numbers))
            else:
                subtotal = 1
                for n in numbers:
                    subtotal *= n
                total += subtotal
                # print()
                # print(subtotal)
            numbers = []
        if c[-1] in ["*", "+"]:
            sign = c[-1]


    return total

part2()
