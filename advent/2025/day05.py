from advent.utils.utils import read_file, printer

TESTING = False
ar = read_file("input")
if TESTING:
    ar = [
"10-14",
"16-20",
"12-18",
"3-5",
"11-21",
"2-3"
    ]

def part1():
    total = 0
    idsmode = True
    ranges = []
    available = []

    for line in ar:
        if idsmode:
            if line == "":
                idsmode = False
                continue
            ranges.append([int(s) for s in line.split("-")])
        else:
            available.append(int(line))


    for a in available:
        fresh = 0
        for r in ranges:
            if a >= r[0] and a <= r[1]:
                fresh = 1
                break

        total += fresh
    return total

@printer
def part2():
    total = 0
    idsmode = True
    ranges = []
    available = []

    for line in ar:
        if idsmode:
            if line == "":
                idsmode = False
                continue
            ranges.append([int(s) for s in line.split("-")])
        else:
            available.append(int(line))


    ranges.sort(key=lambda x: x[0])
    i = 0
    new_ranges = [ranges.pop(0)]
    while i < len(ranges):
        rbmin = ranges[i][0]
        rbmax = ranges[i][1]
        ramin = new_ranges[-1][0]
        ramax = new_ranges[-1][1]
        if  rbmin >= ramin and rbmin <= ramax:
            new_r = [ramin, max(ramax, rbmax)]
            new_ranges.pop()
            new_ranges.append(new_r)
        else:
            new_ranges.append(ranges[i])
        i += 1


    for r in new_ranges:
        print(r)
        total += r[1] - r[0] + 1
        if TESTING:
            for n in range(r[0], r[1]):
                print(n)
    return total



part2()
