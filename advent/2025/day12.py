from advent.utils.utils import printer, read_file, Grid

TESTING = False
ar = read_file("input")
if TESTING:
    ar = read_file("input_test")

class Form:
    def __init__(self, form, num) -> None:
        self.form = []
        self.num = num
        self.size = 0
        for l in form:
            self.size += sum([c == '#' for c in l])

class Region:
    def __init__(self, h, w, qtes) -> None:
        self.height = h
        self.width = w
        self.quantities = qtes

def parse_input():
    forms = []
    regions = []
    i = 0
    while i < len(ar):
        if ':' in ar[i] and 'x' not in ar[i]:
            forms.append(ar[i+1: i+4])
            i += 4
            continue

        if 'x' in ar[i]:
            els = ar[i].split(" ")
            dims = [int(i) for i in els[0][:-1].split("x")]
            regions.append((dims, [int(i) for i in els[1:]]))
        i += 1
    return forms, regions




@printer
def part1():
    total = 1000
    rt = 0
    forms, regions = parse_input()
    fs: list[Form] = []
    rs: list[Region] = []
    for i, f in enumerate(forms):
        fs.append(Form(f, i))
    for r in regions:
        rs.append(Region(r[0][0], r[0][1], r[1]))

    for r in rs:
        if r.height * r.width < sum([i * 9 for i in r.quantities]):
            # print("no way")
            total -= 1
            continue
        else:
            print((r.height/3) * (r.width/3), sum([i  for i in r.quantities]))
            if int((r.height/3) * (r.width/3)) >= sum([i  for i in r.quantities]):
                rt += 1


    return total, rt

part1()


