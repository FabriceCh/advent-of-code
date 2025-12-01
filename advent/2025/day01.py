from advent.utils.utils import read_file

ar = read_file("input.txt")
# ar = [
#     "L68",
#     "L30",
#     "R48",
#     "L5",
#     "R60",
#     "L55",
#     "L1",
#     "L99",
#     "R14",
#     "L82",
# ]

pos = 50
part1 = 0
passwd = 0

for ins in ar:
    dir = ins[0]
    amount = int(ins[1:])
    print("executing", ins)
    if dir == "L":
        for _ in range(amount):
            pos -= 1
            if pos == 0:
                passwd += 1
            if pos < 0:
                pos += 100
    else:
        for _ in range(amount):
            pos += 1
            if pos >= 100:
                pos -= 100
            if pos == 0:
                passwd += 1

    if pos == 0:
        part1 += 1

    print(pos)

print(part1)
print(passwd)
