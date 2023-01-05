lines = []

file = open("/home/fab/AOC/2022/input", "r")
for l in file.readlines():
    lines.append(l.rstrip())
def symbol_to_dec_val(s):
    if s == "2":
        return 2
    if s == "1":
        return 1
    if s == "0":
        return 0
    if s == "-":
        return -1
    if s == "=":
        return -2

def dec_val_to_symbol(v):
    if v == 2:
       return "2"
    if v == 1:
       return "1"
    if v == 0:
       return "0"
    if v == -1:
       return "-"
    if v == -2:
        return "="

def add_single(a, b, r=0):
    dec_val = symbol_to_dec_val(a) + symbol_to_dec_val(b) + symbol_to_dec_val(r)
    ret = "0"
    if dec_val < 3 and dec_val > -3:
        return ret, dec_val_to_symbol(dec_val)
    if dec_val == 3:
        return "1", "="
    if dec_val == 4:
        return "1", "-"
    if dec_val == 5:
        return "1", "0"
    if dec_val == -3:
        return "-", "2"
    if dec_val == -4:
        return "-", "1"
    if dec_val == -5:
        return "-", "0"

def add(a, b):
    if len(b) > len(a):
        a, b = b, a
    if len(a) > len(b):
        b = "".join(["0" for i in range(len(a) - len(b))]) + b
    ans = ""
    r = "0"
    for i in range(len(a)):
        indx = len(a) - (i + 1)
        a_s, b_s = a[indx], b[indx]
        r, val = add_single(a_s, b_s, r)
        ans = val + ans
    if r != "0":
        ans = r + ans
    return ans

def part1():
    ans = "0"
    for line in lines:
        ans = add(ans, line)
    print(ans)

part1()
