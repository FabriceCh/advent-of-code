import heapq
from advent.utils.utils import Grid, read_file

ar = read_file()

# ar = [
#     "###############",
#     "#.......#....E#",
#     "#.#.###.#.###.#",
#     "#.....#.#...#.#",
#     "#.###.#####.#.#",
#     "#.#.#.......#.#",
#     "#.#.#####.###.#",
#     "#...........#.#",
#     "###.#.#####.#.#",
#     "#...#.....#.#.#",
#     "#.#.#.###.#.#.#",
#     "#.....#...#.#.#",
#     "#.###.#.#.#.#.#",
#     "#S..#.....#...#",
#     "###############",
# ]

# ar = [
#     "#################",
#     "#...#...#...#..E#",
#     "#.#.#.#.#.#.#.#.#",
#     "#.#.#.#...#...#.#",
#     "#.#.#.#.###.#.#.#",
#     "#...#.#.#.....#.#",
#     "#.#.#.#.#.#####.#",
#     "#.#...#.#.#.....#",
#     "#.#.#####.#.###.#",
#     "#.#.#.......#...#",
#     "#.#.###.#####.###",
#     "#.#.#...#.....#.#",
#     "#.#.#.#####.###.#",
#     "#.#.#.........#.#",
#     "#.#.#.#########.#",
#     "#S#.............#",
#     "#################",
# ]

# ar = [
#     "##########",
#     "#......E##",
#     "#.##.#####",
#     "#.##.#####",
#     "#S......##",
#     "##########",
# ]

grid = Grid(ar)


class Item:
    def __init__(self, pos, dir, cost, path):
        self.pos = pos
        self.dir = dir
        self.cost = cost
        self.path = path

    def __lt__(self, other):
        return self.cost < other.cost

    def __str__(self):
        return f"cost: {self.cost}, dir: {self.dir}, pos: {self.pos}"


start = (1, 1)
for value, x, y in grid:
    if value == "S":
        start = (x, y)

nexts = [Item(start, ">", 0, {start})]
last_direction = None

part1_answer = 123540

# dijkstra
paths: list[tuple[int, int]] = []
part1 = 0
heapq.heapify(nexts)
seen = {}
while nexts:
    item = heapq.heappop(nexts)
    if grid.get(*item.pos) == "E":
        if paths and item.cost > part1:
            break
        if not paths or item.cost <= part1:
            paths.append(list(item.path))
            part1 = item.cost
    seen[(item.pos, item.dir)] = item.cost
    for neigh in grid.get_full_neighbors_info(*item.pos):
        dir = neigh["dir"]
        val = neigh["val"]
        pos = neigh["pos"]
        new_cost = item.cost + 1
        if item.dir is None or dir != item.dir:
            new_cost += 1000
        if new_cost > part1_answer:
            continue
        if pos in item.path:
            continue
        if (pos, dir) in seen and seen[(pos, dir)] < new_cost:
            continue
        if val != "#":
            new_path = item.path.copy()
            new_path.add(pos)
            heapq.heappush(nexts, Item(pos, dir, new_cost, new_path))


# part1:
print(part1)

all_seen_in_paths = []
for p in paths:
    all_seen_in_paths += p
print(len(set(all_seen_in_paths)))
