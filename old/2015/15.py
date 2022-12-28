import itertools

things = {
    'Sprinkles': {"capacity": 5, "durability": -1, "flavor": 0, "texture": 0, "calories": 5},
    'PeanutButter': {"capacity": -1, "durability": 3, "flavor": 0, "texture": 0, "calories": 1},
    'Frosting': {"capacity": 0, "durability": -1, "flavor": 4, "texture": 0, "calories": 6},
    'Sugar': {"capacity" :-1, "durability": 0, "flavor": 0, "texture": 2, "calories": 8}
}

things = {
    "Butterscotch": {"capacity": -1, "durability": -2, "flavor": 6, "texture": 3, "calories;": 8},
    "Cinnamon": {"capacity": 2, "durability": 3, "flavor": -2, "texture": -1, "calories;": 3}
}

combs = list(itertools.combinations(list(things.keys()), 100))

def get_score(ingrs):
    cap, dur, fla, tex, cal = 0, 0, 0, 0, 0

    for ing in ingrs:
        cap += things[ing]["capacity"]
        dur += things[ing]["durability"]
        fla += things[ing]["flavor"]
        tex += things[ing]["texture"]
    return cap * dur * fla * tex

ma = 0
print(len(combs))
for c in combs:
    ma = max(ma, get_score(c))
print(ma)