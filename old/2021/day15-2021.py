import heapq
import copy

def read_file(path):
    arr = []
    with open(path, "r") as file:
        for line in file:
            arr.append(line.rstrip())
    return arr

ar = read_file("input")

_map = []
for line in ar:
    _map.append([int(a) for a in line])

def increment_map(a_map):
    new_map = copy.deepcopy(a_map)
    for y, line in enumerate(new_map):
        for x, el in enumerate(line):
            new_map[y][x] = int(el) + 1
            if el == 9:
                new_map[y][x] = 1
    return new_map

def extend_map():
    # right extend
    new_map = copy.deepcopy(_map)
    inc_map = copy.deepcopy(_map)
    for i in range(4):
        inc_map = increment_map(inc_map)
        for l, line in enumerate(new_map):
            line += copy.deepcopy(inc_map[l])
    
    # down extend
    inc_map = copy.deepcopy(new_map)
    for i in range(4):
        inc_map = increment_map(inc_map)
        new_map += copy.deepcopy(inc_map)
    return new_map

_map = extend_map()
#for l in _map:
#    print(l)

X_LEN = len(_map[0])
Y_LEN = len(_map)

def get_neighbors(x, y):
    neigs = []
    if x != 0:
        neigs.append((x - 1, y))
    if x != X_LEN - 1:
        neigs.append((x +1, y))
    if y != 0:
        neigs.append((x, y - 1))
    if y != Y_LEN - 1:
        neigs.append((x, y + 1))
    return neigs

print("starting disjktra")

def disjktra():
    
    start = (0,0)
    seen = {start}
    target = (X_LEN-1, Y_LEN-1)
    dist = {start: 0}
    nodes_to_visit = [(_map[0][0], start)]
    heapq.heapify(nodes_to_visit)
    iter = 0
    while nodes_to_visit:
        current_node = heapq.heappop(nodes_to_visit)
        dist[current_node[1]] = int(current_node[0])
        if current_node[1] == target:
            break
        
        neigs = get_neighbors(current_node[1][0], current_node[1][1])
        for n in neigs:
            if n not in seen:
                dist[n] = dist[current_node[1]]
                seen.add(n)
                heapq.heappush(nodes_to_visit, (int(dist[current_node[1]]) + int(_map[n[1]][n[0]]), n))
        iter += 1
        print(iter)
    print(dist[target] - dist[start])

disjktra()