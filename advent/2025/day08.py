from typing import Set
from advent.utils.utils import printer, read_file
import math

TESTING = False
ar = read_file("input")
if TESTING:
    ar = [
    "162,817,812",
    "57,618,57",
    "906,360,560",
    "592,479,940",
    "352,342,300",
    "466,668,158",
    "542,29,236",
    "431,825,988",
    "739,650,466",
    "52,470,668",
    "216,146,977",
    "819,987,18",
    "117,168,530",
    "805,96,715",
    "346,949,466",
    "970,615,88",
    "941,993,340",
    "862,61,35",
    "984,92,344",
    "425,690,689",
    ]
    N = 10
else:
    N = 1000


class Box:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.connections: Set[Box] = set()
    
    def find_all(self):
        queue = set().union(self.connections)
        seen = set().union(queue)
        seen.add(self)
        while queue:
            item = queue.pop()
            for b in item.connections:
                if b not in seen:
                    queue.add(b)
                    seen.add(b)
        return seen


class Dist:
    def __init__(self, b1, b2, dist):
        self.b1 = b1
        self.b2 = b2
        self.dist = dist

def connect(b1: Box, b2: Box):
    graph1 = b1.find_all()
    if b2 not in graph1:
        b2.connections.add(b1)
        b1.connections.add(b2)
        print(b1.x * b2.x)

def distance (b1: Box, b2: Box):
    return math.sqrt(sum([(b1.x - b2.x)**2, (b1.y - b2.y)**2, (b1.z - b2.z)**2]))

boxes: list[Box] = []
for line in ar:
    numbers = line.split(",")
    boxes.append(Box(numbers[0], numbers[1], numbers[2]))


# @printer
def part1():
    distances: list[Dist] = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            b1, b2 = boxes[i], boxes[j]
            dist = distance(boxes[i], boxes[j])
            distances.append(Dist(b1, b2, dist))
    
    distances.sort(key=lambda b: b.dist)
    for d in distances[:N]:
        connect(d.b1, d.b2)

    seen = set()
    graphs = []
    for b in boxes:
        if b not in seen:
            graphs.append(b.find_all())
            seen = seen.union(graphs[-1])
    total = 1
    graphs.sort(key= lambda x: len(x))
    for i in range(1,4):
        total *= len(graphs[-i])
        print(len(graphs[-i]))
    return total

# part1()

def part2():
    distances: list[Dist] = []
    print("computing distances")
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            b1, b2 = boxes[i], boxes[j]
            dist = distance(boxes[i], boxes[j])
            distances.append(Dist(b1, b2, dist))
    
    print("sorting distances")
    distances.sort(key=lambda b: b.dist)
    print("connecting distances")
    for d in distances:
        connect(d.b1, d.b2)
        if len(boxes[0].find_all()) == 1000:
            break


part2()

