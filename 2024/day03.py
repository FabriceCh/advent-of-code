import re
from utils import read_file

# part 1
ar = read_file("2024/input")
# ar = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
line = "".join(ar)


def process_line(line):
    pattern = r"(mul\([0-9]{1,3},[0-9]{1,3}\))"
    matches = re.findall(pattern, line)
    result = 0
    for match in matches:
        halves = match.split(",")
        to_add = int(halves[0][4:]) * int(halves[1][:-1])
        result += to_add
    return result


answer = process_line(line)

print(answer)


# part 2
def process(line):
    mul_pattern = r"(mul\([0-9]{1,3},[0-9]{1,3}\))"
    do_pattern = r"(do())"
    dont_pattern = r"(don't())"
    do_positions = [0]
    dont_positions = [-1]
    do_cursor = 0
    dont_cursor = 0
    result = 0
    for m in re.finditer(do_pattern, line):
        do_positions.append(m.span()[1])

    for m in re.finditer(dont_pattern, line):
        dont_positions.append(m.span()[1])
    do_positions.append(100000000)
    dont_positions.append(100000000)

    for m in re.finditer(mul_pattern, line):
        while do_positions[do_cursor + 1] < m.span()[1]:
            do_cursor += 1
        while dont_positions[dont_cursor + 1] < m.span()[1]:
            dont_cursor += 1
        if do_positions[do_cursor] > dont_positions[dont_cursor]:
            match = m.group()
            halves = match.split(",")
            to_add = int(halves[0][4:]) * int(halves[1][:-1])
            result += to_add
    return result


print(process(line))
