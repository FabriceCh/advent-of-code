import heapq
from aocd import get_data
ar = get_data(day=12, year=2022)
ar = ar.splitlines()

#print(ar)

ar2 = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi",
]

_map = []
for line in ar:
    _map.append([ord(a) for a in line])

X_LEN = len(_map[0])
Y_LEN = len(_map)

def find_S(ar):
    for i, line in enumerate(ar):
        for j, el in enumerate(line):
            if el == "S":
                return [i, j]

def find_E(ar):
    for i, line in enumerate(ar):
        for j, el in enumerate(line):
            if el == "E":
                return [i, j]

def find_as(ar):
    aas = []
    for i, line in enumerate(ar):
        for j, el in enumerate(line):
            if el == "a":
                aas.append([i, j])
    return aas

def get_neighbors(x, y):
    neigs = []
    if x != 0:
        neigs.append((x - 1, y))
    if x != Y_LEN - 1:
        neigs.append((x +1, y))
    if y != 0:
        neigs.append((x, y - 1))
    if y != X_LEN - 1:
        neigs.append((x, y + 1))
    return neigs

get_neighbors(4, 4)

def disjktra(start, end):
    
    start = tuple(start)
    seen = {start}
    target = tuple(end)
    dist = {start: 0}
    nodes_to_visit = [(_map[0][0], start)]
    heapq.heapify(nodes_to_visit)
    iter = 0
    while nodes_to_visit:

        current_node = heapq.heappop(nodes_to_visit)
        if current_node[1] == target:
            break
        
        neigs = get_neighbors(current_node[1][0], current_node[1][1])
        for n in neigs:
            
            
            if _map[current_node[1][0]][current_node[1][1]] == ord("S"):
                cur_height = ord("a")
            else:
                cur_height = _map[current_node[1][0]][current_node[1][1]]
            
            if _map[n[0]][n[1]] == ord("E"):
                n_height = ord("z")
            else:
                n_height = _map[n[0]][n[1]]


            is_not_too_high = cur_height >= n_height - 1
            if n not in seen and is_not_too_high:
                dist[n] = dist[current_node[1]] + 1
                seen.add(n)
                heapq.heappush(nodes_to_visit, (int(dist[current_node[1]]) + 1, n))
        iter += 1
    if target in dist.keys():
        print(dist[target])
        return dist[target]
    else:
        return 10000

def part1():
    start = find_S(ar)
    end = find_E(ar)
    print(start, end)
    print(disjktra(start, end))

def part2():
    starts = find_as(ar)
    end = find_E(ar)
    ans = 10000
    for s in starts:
        ans = min(ans, disjktra(s, end))
    print(ans)
part1()
part2()

#print(get_neighbors(4, 4))