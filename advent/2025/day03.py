from advent.utils.utils import read_file
from itertools import combinations

ar = read_file("input")
# ar = [
# "987654321111111",
# "811111111111119",
# "234234234234278",
# "818181911112111",
# ]
# part 1
total = 0

for line in ar:
    max1, max2 = "0", "0"
    for n in line:
        if n > max1:
            max2 = max1
            max1 = n
        elif n > max2:
            max2 = n
    if line.index(max1) > line.index(max2):
        if line.index(max1) != len(line) - 1:
            max2 = "0"
            for i in range(line.index(max1) + 1, len(line)):
                if line[i] > max2:
                    max2 = line[i]
        else:
            max1, max2 = max2, max1


    total += int(max1 + max2)

print(total)

#part2
total = 0
for line in ar:
    ans = []
    remaining = 12
    for _ in range(12):
        obligatory_slice_size = len(line) - (remaining - 1)
        obslice = line[:obligatory_slice_size]
        ans.append(max(obslice))
        line = line[line.index(max(obslice)) + 1:]
        remaining -= 1
    total += int("".join(ans))


print(total)
