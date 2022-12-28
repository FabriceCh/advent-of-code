from utils import read_file

lines = read_file("/home/fabrice/advent-of-code/2022/input")
lines2 = [
    "1",
    "2",
    "-3",
    "3",
    "-2",
    "0",
    "4",
]

def part1():
    keyy = 811589153
    numbers = [int(l) * keyy for l in lines]
    numbers = [(i,n) for i, n in enumerate(numbers)]
    length = len(numbers)
    print([i[1] for i in numbers])
    for _ in range(10):
        for i in range(len(numbers)):
            current_idx = None
            for j, n in enumerate(numbers):
                if n[0] == i:
                    current_idx = j
                    break
            nnn = numbers.pop(current_idx)
            new_pos = (current_idx + nnn[1]) % (length - 1)
            numbers.insert(new_pos, nnn)
            #print(nnn)
            #print([i[1] for i in numbers])

    zero_idx = None
    for j, n in enumerate(numbers):
            if n[1] == 0:
                zero_idx = j
                break
    val_1k = numbers[(zero_idx + 1000) % len(numbers)][1]
    val_2k = numbers[(zero_idx + 2000) % len(numbers)][1]
    val_3k = numbers[(zero_idx + 3000) % len(numbers)][1]
    print(val_1k, val_2k, val_3k)
    print(val_1k + val_2k + val_3k)

part1()
