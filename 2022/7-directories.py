from utils import read_file

ar = read_file("/home/fabrice/advent-of-code/2022/input")

current_in = []
sizes = {"/": 0}
seen_file = {}

def add_to_dict(dic, key, value):
    if key in dic.keys():
        dic[key] += value
    else:
        dic[key] = value

for l in ar:
    args = l.split(" ")
    pwd = "".join(current_in)
    if args[1] == "cd" and  args[2] != "..":
        current_in.append(args[2])
    if args[1] == "cd" and args[2] == "..":
        current_in.pop()
    if args[0] != "$" and args[0] != "dir":
        f = args[1]
        
        if pwd in seen_file.keys() and f in seen_file[pwd]:
            continue
        else:
            add_to_dict(seen_file, pwd, [f])
            ppwd = ""
            for dir in current_in:
                ppwd += dir
                add_to_dict(sizes, ppwd, int(args[0]))

# part 1
to = 0
for d in sizes.values():
    if d <= 100000:
        to += d
print(to)

# part 2
min_for_prog = 30000000
total_space = sizes["/"]
tootal = 70000000
remaining = tootal - total_space
to_be_deleted = min_for_prog - remaining
all_sizes = list(sizes.values())
all_sizes.sort()
for s in all_sizes:
    if s > to_be_deleted:
        print(s)
        break
