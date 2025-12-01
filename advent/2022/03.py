from utils import read_file

ar = read_file("/home/fabrice/advent-of-code/2022/input")
a = [
    'vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw',
]

def letter_to_priority(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 64  + 26

def part1(ar):
    priorities_sum = 0
    for line in ar:
        half_1 = line[0:len(line)//2]
        half_2 = line[len(line)//2:]
        for l in half_2:
            if l in half_1:
                priorities_sum += letter_to_priority(l)
                break
    print(priorities_sum)

def part2(ar):
    priorities_sum = 0
    for i in range (0, len(ar), 3):
        for l in ar[i]:
            if l in ar[i + 1] and l in ar[i + 2]:
                priorities_sum += letter_to_priority(l)
                break
    print(priorities_sum)

part2(ar)