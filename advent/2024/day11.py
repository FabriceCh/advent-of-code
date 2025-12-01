from functools import cache


line = "510613 358 84 40702 4373582 2 0 1584"
# line = "125 17"
# line = "2024"

stones = line.split(" ")
stones = [int(s) for s in stones]


# part 1
@cache
def single_blink(stone):
    stone_str = str(stone)
    digits = len(stone_str)
    if stone == 0:
        return 1, None
    elif digits % 2 == 0:
        return int(stone_str[: digits // 2]), int(stone_str[digits // 2 :])
    else:
        return stone * 2024, None


def blink(stones):
    new_stones = []
    for s in stones:
        s1, s2 = single_blink(s)
        new_stones.append(s1)
        if s2 is not None:
            new_stones.append(s2)
    return new_stones


for i in range(25):
    # print(i)
    # print(stones)
    stones = blink(stones)

print(len(stones))


# part 2
@cache
def mega_blink(stone: int, bli: int) -> int:
    new_stones = [s for s in single_blink(stone) if s is not None]
    if bli == 1:
        return len(new_stones)
    result = 0
    for s in new_stones:
        result += mega_blink(s, bli - 1)
    return result


answer = 0
for s in stones:
    answer += mega_blink(s, 75)

print(answer)
