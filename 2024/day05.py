from typing import Dict, Set
from utils import read_file

ar = read_file("2024/input")
# ar = [
#     "47|53",
#     "97|13",
#     "97|61",
#     "97|47",
#     "75|29",
#     "61|13",
#     "75|53",
#     "29|13",
#     "97|29",
#     "53|29",
#     "61|53",
#     "97|53",
#     "61|29",
#     "47|13",
#     "75|47",
#     "97|75",
#     "47|61",
#     "75|61",
#     "47|29",
#     "75|13",
#     "53|13",
#     "",
#     "75,47,61,53,29",
#     "97,61,53,29,13",
#     "75,29,13",
#     "75,97,47,61,53",
#     "61,13,29",
#     "97,13,75,29,47",
# ]

raw_rules = [line for line in ar if "|" in line]
raw_updates = [line for line in ar if "," in line]

rules: Dict[int, Set[int]] = {}
for rr in raw_rules:
    nums = [int(i) for i in rr.split("|")]
    if nums[0] not in rules:
        rules[nums[0]] = {nums[1]}
    else:
        rules[nums[0]].add(nums[1])

updates = [[int(i) for i in line.split(",")] for line in raw_updates]

count = 0

# part 1
incorrect_updates = []
for update in updates:
    befores = []
    correct = True
    for number in update:
        for prev in befores:
            if number in rules and prev in rules[number]:
                correct = False
                break
        if not correct:
            break
        befores.append(number)
    if correct:
        count += update[len(update) // 2]
    else:
        incorrect_updates.append(update)

print(count)
# part 2
# Would it work to pop [number] and insert it right before [previous number]? do that until it is 'correct', we assume there's at least 1 order that is possible

count = 0

update: list
for update in incorrect_updates:
    correct = False
    while not correct:
        correct = True
        befores = []
        for index, number in enumerate(update):
            for prev_index, prev in enumerate(befores):
                if number in rules and prev in rules[number]:
                    n = update.pop(index)
                    update.insert(prev_index, n)
                    correct = False
            befores.append(number)

    count += update[len(update) // 2]

# should be 123 for test input
print(count)
