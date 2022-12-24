from utils import read_file

ar = read_file("/home/fabrice/advent-of-code/2022/input")
ar2 = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",

]
def parse_line(line):
    pairs = line.split(",")
    rs1, rs2 = pairs[0].split("-"), pairs[1].split("-")
    return int(rs1[0]), int(rs1[1]), int(rs2[0]), int(rs2[1])

countr = 0
for l in ar:
    min1, max1, min2, max2 = parse_line(l)
    if max1 >= min2 and max1 <= max2:
        countr += 1
    elif max2 >= min1 and max2 <= max1:
        countr += 1


print(countr)