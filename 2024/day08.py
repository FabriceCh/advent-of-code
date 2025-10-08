from utils import read_file, Grid

ar = read_file("2024/input")
# ar = [
#     "............",
#     "........0...",
#     ".....0......",
#     ".......0....",
#     "....0.......",
#     "......A.....",
#     "............",
#     "............",
#     "........A...",
#     ".........A..",
#     "............",
#     "............",
# ]

grid = Grid(ar)

towers = {}
for c, x, y in grid:
    if c == ".":
        continue
    if c in towers:
        towers[c].append((x, y))
    else:
        towers[c] = [(x, y)]


def compute_distance(pos1, pos2):
    return (pos1[0] - pos2[0], pos1[1] - pos2[1])


def find_antinodes(towers_pos: list):
    antinodes = []
    for i, pos1 in enumerate(towers_pos):
        for pos2 in towers_pos[i + 1 : :]:
            dist = compute_distance(pos1, pos2)
            node1, node2 = (
                (pos1[0] + dist[0], pos1[1] + dist[1]),
                compute_distance(pos2, dist),
            )
            antinodes += [node1, node2]
    return antinodes


def find_antinodes_part2(towers_pos: list):
    antinodes = [pp for pp in towers_pos]
    for i, pos1 in enumerate(towers_pos):
        for pos2 in towers_pos[i + 1 : :]:
            dist = compute_distance(pos1, pos2)
            p1, p2 = pos1, pos2
            # times height is overkill and wastes some time but it works
            for _ in range(grid._height):
                node1, node2 = (
                    (p1[0] + dist[0], p1[1] + dist[1]),
                    compute_distance(p2, dist),
                )
                p1, p2 = node1, node2
                antinodes += [node1, node2]
    return antinodes


all_antinodes = set()
for totos in towers.values():
    for antinode in find_antinodes_part2(totos):
        if not grid.is_out_of_bounds(antinode[0], antinode[1]):
            all_antinodes.add(antinode)

for anti in all_antinodes:
    grid.set(anti[0], anti[1], "#")
print(len(all_antinodes))
