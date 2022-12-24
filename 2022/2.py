from utils import read_file

ar = read_file("/home/fabrice/advent-of-code/2022/input")

#ar = [
#    "A Y",
#    "B X",
#    "C Z"
#]

#b = [  for a in ar]

total = 0

valus = {
    "A": 1, "B": 2, "C": 3
}

for i, a in enumerate(ar):
    f, s = a[0], a[2]
    win = False
    draw = False
    lose = False
    sum = 0

    if s == "X":
        lose = True
    elif s == "Y":
        draw = True
    elif s == "Z":
        win = True

    if win:
        sum += 6
    elif draw: 
        sum += 3
    
    if draw:
        sum += valus[f]
    
    if lose:
        if f == "A":
            sum += 3
        if f == "B":
            sum += 1
        if f == "C":
            sum += 2

    if win:
        if f == "A":
            sum += 2
        if f == "B":
            sum += 3
        if f == "C":
            sum += 1
    print(win)
    print(sum)
    total += sum

print(total)
