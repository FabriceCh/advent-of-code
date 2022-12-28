from aocd import get_data
ar = get_data(day=11, year=2015)
ar = ar.splitlines()
print(ar)

def increment(password):
    new_pasword = list(password)
    for i, letter in enumerate(list(password[::-1])):
        if letter == "z":
            new_pasword[len(password) - 1 - i] = "a"
        else:
            new_pasword[len(password) - 1 - i] = chr(ord(letter) + 1)
            break
    return "".join(new_pasword)


def is_increasing_straight(password):
    for i, letter in enumerate(password[:-2]):
        if ord(letter) + 1 == ord(password[i+1]) and ord(letter) + 2 == ord(password[i+2]):
            return True
    return False


def isnt_confusing(password):
    return not("i" in password or "o" in password or "l" in password)
            
def is_pair(password):
    pairs = []
    for i, letter in enumerate(password[:-1]):
        if letter == password[i + 1]:
            pairs.append((i, i+1))
    if len(pairs) < 2:
        return False
    if len(pairs) > 2:
        return True
    if pairs[0][1] != pairs[1][0]:
        return True
    return False

def part1(pwd):
    while not(is_increasing_straight(pwd)) or not(isnt_confusing(pwd)) or not(is_pair(pwd)):
        pwd = increment(pwd)
    print(pwd)

part1("cqjxxyzz")

def part2(pwd):
    pwd = increment(pwd)
    part1(pwd)

part2("cqjxxyzz")
