from advent.utils.utils import read_file

ar = read_file("input")
# ar = ["""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124"""]

total = 0

line = ar[0]
ranges = [a for a in line.split(",")]
ranges = [r.split("-") for r in ranges ]

def find_divisors_sqrt(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)


for r in ranges:
    for i in range(int(r[0]), int(r[1]) + 1):
        s = str(i)
        divisors = find_divisors_sqrt(len(s)) #divisors is just [2] for part 1 i guess
        for d in divisors:
            slice_len = len(s)//d
            n_slice = d
            slices = [ s[i*slice_len:i*slice_len + slice_len] for i in range(n_slice) ]
            if len(slices) == 1:
                continue
            all_eq = True
            for si in range(len(slices) -1):
                if slices[si] != slices[si+1]:
                    all_eq = False
                    break
            if all_eq:
                total += i
                break
            
print(total)

