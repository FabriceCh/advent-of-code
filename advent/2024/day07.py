from utils import read_file

ar = read_file("2024/input")
# ar = [
#     "190: 10 19",
#     "3267: 81 40 27",
#     "83: 17 5",
#     "156: 15 6",
#     "7290: 6 8 6 15",
#     "161011: 16 10 13",
#     "192: 17 8 14",
#     "21037: 9 7 18 13",
#     "292: 11 6 16 20",
# ]

equations = [
    (
        int(line.split(":")[0]),
        [int(num) for num in line.split(":")[1].split(" ") if num != ""],
    )
    for line in ar
]


def is_equation_true(eq):
    res = eq[0]
    nums = eq[1]
    outcomes = [nums.pop(0)]
    for num in nums:
        new_out = []
        for outcome in outcomes:
            # for part1: new_out += [outcome + num, outcome * num]
            new_out += [outcome + num, outcome * num, int(str(outcome) + str(num))]
        outcomes = new_out
    return res in outcomes


counter = 0

for eq in equations:
    if is_equation_true(eq):
        counter += eq[0]

print(counter)
