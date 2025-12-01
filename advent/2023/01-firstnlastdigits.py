from utils import read_file

ar = read_file("2023/input")
ar2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

cumm = 0
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
mapn = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}

new_ar = ["" for _ in range(len(ar))]

for eli, el in enumerate(ar):
    for i, let in enumerate(el):
        if let in numbers:
            new_ar[eli] += str(let)
            continue
        for strn, intn in mapn.items():
            if len(el) - i >= len(strn):
                if el[i : i + len(strn)] == strn:
                    new_ar[eli] += str(intn)
                    continue


print(new_ar)


for e in new_ar:  # switch to 'ar' for part 1
    first = ""
    last = ""
    for letter in e:
        if letter in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            if first == "":
                first = letter
            else:
                last = letter

    if last == "":
        last = first
    number = int(first + last)
    print(number)
    cumm += number

print(cumm)
