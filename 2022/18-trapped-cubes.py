from utils import read_file

lines = read_file("/home/fabrice/advent-of-code/2022/input")


def line_to_position(line):
    return tuple([int(a) for a in line.split(",")])


positions = [line_to_position(l) for l in lines]


def get_adjacent_positions(p):
    adjacents = []
    adjacents.append((p[0] - 1, p[1], p[2]))
    adjacents.append((p[0] + 1, p[1], p[2]))
    adjacents.append((p[0], p[1] - 1, p[2]))
    adjacents.append((p[0], p[1] + 1, p[2]))
    adjacents.append((p[0], p[1], p[2] - 1))
    adjacents.append((p[0], p[1], p[2] + 1))
    return adjacents


def is_position_trapped(p, beams):
    xy, xz, yz = ("z", p[0], p[1]), ("y", p[0], p[2]), ("x", p[1], p[2])
    if xy not in beams.keys() or xz not in beams.keys() or yz not in beams.keys():
        return False
    is_between_z = (p[2] < sorted(beams[xy], key=lambda x: x[0])[-1][0] and p[2] > sorted(beams[xy], key=lambda x: x[0])[0][0])
    is_between_y = (p[1] < sorted(beams[xz], key=lambda x: x[0])[-1][0] and p[1] > sorted(beams[xz], key=lambda x: x[0])[0][0])
    is_between_x = (p[0] < sorted(beams[yz], key=lambda x: x[0])[-1][0] and p[0] > sorted(beams[yz], key=lambda x: x[0])[0][0])
    return (is_between_x and is_between_y and is_between_z)


class Trapper:

    def __init__(self):
        self.trapped = {}

    def is_pos_really_trapped(self, p, cubes, beams):

        if p in self.trapped.keys():
            return self.trapped[p]

        pile = [p]
        seen = set()
        while pile:
            cur = pile.pop()
            seen.add(cur)
            if not is_position_trapped(cur, beams):
                for pp in seen:
                    self.trapped[pp] = False
                return False
            else:
                adjs = get_adjacent_positions(cur)
                for a in adjs:
                    if a not in cubes and a not in seen:
                        pile.append(a)
        for pp in seen:
            self.trapped[pp] = True
        return True


def solve(positions):
    beams = {}
    seen_cubes = set()
    for p in positions:
        seen_cubes.add(p)
        p_beams = [("z", p[0], p[1], p[2]), ("y", p[0], p[2], p[1]), ("x", p[1], p[2], p[0])]
        for b in p_beams:
            beam = (b[0], b[1], b[2])
            val = b[3]
            if beam in beams.keys():
                beams[beam].append((val, p))
            else:
                beams[beam] = [(val, p)]
    t = Trapper()
    part1_ans = 0
    answer = 0
    for p in positions:
        adjs = get_adjacent_positions(p)
        for a in adjs:
            if a not in seen_cubes:
                part1_ans += 1
                if not t.is_pos_really_trapped(a, seen_cubes, beams):
                    answer += 1
    print("part1:", part1_ans)
    print(answer)

solve(positions)
