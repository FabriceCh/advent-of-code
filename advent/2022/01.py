from utils import read_file

ar = read_file("/home/fabrice/advent-of-code/2022/input")

#b = [  for a in ar]

ctr = 0
elves = {}

for i, a in enumerate(ar):
    if a == "":
        ctr += 1
    else:
        if ctr in elves.keys():
            elves[ctr] += int(a)
        else:
            elves[ctr] = int(a)

max = 0
for bb in elves.values():
    if bb > max:
        max = bb

lister = list(elves.values())
lister = sorted(lister)
print(lister[-3:])
print(sum(lister[-3:]))
#print(max)
