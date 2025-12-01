from utils import read_file

ar = read_file("/home/fabrice/advent-of-code/2022/input")
ar = ar[10:]

print(ar[0])
a = [" ",
    "H", 
    "M", 
    "P", 
    "Z", ]

piles = {
    1: ["R",
        "H",
        "M",
        "P",
        "Z",],
    2: [
        "B",
        "J",
        "C",
        "P",
        ],
    3: [
        "D",
        "C",
        "L",
        "G",
        "H",
        "N",
        "S",
    ],
    4: [
        "L",
        "R",
        "S",
        "Q",
        "D",
        "M",
        "T",
        "F",
    ],
    5: ["M",
        "Z",
        "T",
        "B",
        "Q",
        "P",
        "S",
        "F",],
    6: [
        "G",
        "B",
        "Z",
        "S",
        "F",
        "T",
    ],
    7: [
        "V",
        "R",
        "N",
    ],
    8: [
        "M",
        "C",
        "V",
        "D",
        "T",
        "L",
        "G",
        "P",
    ],
    9: [
        "L",
        "M",
        "F",
        "J",
        "N",
        "Q",
        "W",
    ],
}

for k, p in piles.items():
    piles[k] = p[::-1]

def text_to_nums(l):
    words = l.split(" ")
    return int(words[1]), int(words[3]),int(words[5])
print(len(piles[9]))

for l in ar:
    move, fr, too = text_to_nums(l)
    print(l)
    #for n in range(move):
    #    aa = piles[fr].pop()
    #    piles[too] = piles[too] + [aa]
    stack = piles[fr][-move:]
    piles[fr] = piles[fr][:-move]
    piles[too] += stack
    print(piles)

strr = ""
for p in piles.values():
    strr += p[-1]
print(strr)