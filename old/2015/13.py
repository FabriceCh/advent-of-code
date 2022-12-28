import itertools
from typing import List
from aocd import get_data
ar = get_data(day=13, year=2015)
ar = ar.splitlines()


ar2 = [
    "Alice would gain 54 happiness units by sitting next to Bob.",
    "Alice would lose 79 happiness units by sitting next to Carol.",
    "Alice would lose 2 happiness units by sitting next to David.",
    "Bob would gain 83 happiness units by sitting next to Alice.",
    "Bob would lose 7 happiness units by sitting next to Carol.",
    "Bob would lose 63 happiness units by sitting next to David.",
    "Carol would lose 62 happiness units by sitting next to Alice.",
    "Carol would gain 60 happiness units by sitting next to Bob.",
    "Carol would gain 55 happiness units by sitting next to David.",
    "David would gain 46 happiness units by sitting next to Alice.",
    "David would lose 7 happiness units by sitting next to Bob.",
    "David would gain 41 happiness units by sitting next to Carol.",
]

def text_to_values(text):
    words = text.split(" ")
    subject = words[0]
    other = words[-1][:-1]
    effect, amount = words[2], int(words[3])
    if effect == "lose":
        amount *= -1
    return subject, other, amount

def compute_total_happiness(arrangement: List[str], effects):
    total = 0
    for i, person in enumerate(arrangement):
        total += effects[person][arrangement[i - 1]]
        if i == len(arrangement) - 1:
            total += effects[person][arrangement[0]]
        else:
            total += effects[person][arrangement[i + 1]]
    return total

def part1():

    effects = {}

    for line in ar:
        subject, other, amount = text_to_values(line)
        if subject not in effects.keys():
            effects[subject] = {other: amount}
        else:
            effects[subject][other] = amount
    
    people = effects.keys()
    arrangements = list(itertools.permutations(people))
    h = 0
    for aa in arrangements:
        h = max(h, compute_total_happiness(aa, effects))
    print(h)
    return h

def part2():
    prev_h = part1()
    effects = {}

    for line in ar:
        subject, other, amount = text_to_values(line)
        if subject not in effects.keys():
            effects[subject] = {other: amount}
        else:
            effects[subject][other] = amount
    # add myself
    effects["Fab"] = {k: 0 for k in effects.keys()}
    for k in effects.keys():
        effects[k]["Fab"] = 0
    print(effects)

    people = effects.keys()
    arrangements = list(itertools.permutations(people))
    h = 0
    aaa = []
    for aa in arrangements:
        new_h = compute_total_happiness(aa, effects)
        if new_h > h:
            h = new_h
            aaa = aa
    print(aaa)
    print(h)
    

part1()
part2()