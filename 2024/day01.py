from utils import read_file, count_occurences

# part 1
ar = read_file("2024/input")
l1, l2 = [], []
for line in ar:
    numbers = [int(n) for n in line.split("   ")]
    l1.append(numbers[0])
    l2.append(numbers[1])

l1.sort()
l2.sort()

distances = [int(abs(n1 - n2)) for n1, n2 in zip(l1, l2)]
print(sum(distances))

# part 2
right_list_occurences = count_occurences(l2)
ans = 0
for n in l1:
    if not right_list_occurences.get(n):
        continue
    ans += n * right_list_occurences.get(n)

print(ans)
