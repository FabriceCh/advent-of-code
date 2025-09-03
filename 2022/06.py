from utils import read_file

ar = read_file("/home/fabrice/advent-of-code/2022/input")[0]
a = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

def part1(ar):
    last_3 = ar[0:3]
    for i in range(3, len(ar)):
        if ar[i] not in last_3 and len(set(list(last_3))) == 3:
            print(i + 1)
            break
        else:
            last_3 = last_3[1:]  + ar[i]

def part2(ar):
    last_13 = ar[0:13]
    for i in range(13, len(ar)):
        if ar[i] not in last_13 and len(set(list(last_13))) == 13:
            print(i + 1)
            break
        else:
            last_13 = last_13[1:]  + ar[i]

part2(ar)