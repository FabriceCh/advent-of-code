import re
from advent.utils.utils import read_file


ar = read_file("input.txt")
# ar = [
#     "Button A: X+94, Y+34",
#     "Button B: X+22, Y+67",
#     "Prize: X=8400, Y=5400",
#     "",
#     "Button A: X+26, Y+66",
#     "Button B: X+67, Y+21",
#     "Prize: X=12748, Y=12176",
#     "",
#     "Button A: X+17, Y+86",
#     "Button B: X+84, Y+37",
#     "Prize: X=7870, Y=6450",
#     "",
#     "Button A: X+69, Y+23",
#     "Button B: X+27, Y+71",
#     "Prize: X=18641, Y=10279",
#     "",
# ]


class Machine:
    def __init__(self, a_x=0, a_y=0, b_x=0, b_y=0, prize_x=0, prize_y=0):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.prize_x = prize_x
        self.prize_y = prize_y

    def multiply_and_compare(self, a_mult, b_mult):
        return (self.a_x * a_mult + self.b_x * b_mult == self.prize_x) and (
            self.a_y * a_mult + self.b_y * b_mult == self.prize_y
        )

    def find_optimal_tokens(self):
        min_tokens = 1000
        for a_mult in range(101):
            for b_mult in range(101):
                if self.multiply_and_compare(a_mult, b_mult):
                    min_tokens = min(min_tokens, (a_mult * 3) + b_mult)
        return min_tokens


machines: list[Machine] = []
current_machine = Machine()

for line in ar:
    pattern = r"[\+,\=]([0-9]*)"
    matches = re.findall(pattern=pattern, string=line)
    # print(matches)
    if line.startswith("Button A"):
        current_machine.a_x = int(matches[0])
        current_machine.a_y = int(matches[2])
    if line.startswith("Button B"):
        current_machine.b_x = int(matches[0])
        current_machine.b_y = int(matches[2])
    if line.startswith("Prize"):
        current_machine.prize_x = int(matches[0])
        current_machine.prize_y = int(matches[2])
    # add a final enter in input to make this work
    if line == "":
        machines.append(current_machine)
        current_machine = Machine()


total_tokens = 0
for m in machines:
    # print(f"Prize {m.prize_x}, {m.prize_y}")
    # print(f"A {m.a_x}, {m.a_y}")
    # print(f"B {m.b_x}, {m.b_y}")
    # print()
    tokens = m.find_optimal_tokens()
    if tokens != 1000:
        total_tokens += tokens

print(total_tokens)


# part 2
def algebra(m: Machine):
    ax, ay, bx, by, px, py = m.a_x, m.a_y, m.b_x, m.b_y, m.prize_x, m.prize_y
    top = py * ax - ay * px
    bot = by * ax - ay * bx
    b_mult = top / bot
    a_mult = (px - bx * b_mult) / ax
    if a_mult == int(a_mult) and b_mult == int(b_mult):
        return int(a_mult) * 3 + int(b_mult)
    return 0


total_tokens = 0
for m in machines:
    m.prize_x += 10000000000000
    m.prize_y += 10000000000000
    total_tokens += algebra(m)
    if algebra(m) == 0:
        print(f"Prize {m.prize_x}, {m.prize_y}")
print(total_tokens)
