from typing import Tuple
from advent.utils.utils import read_file
from functools import cache

ar = read_file("input")

# ar = [
# "svr: aaa bbb",
# "aaa: fft",
# "fft: ccc",
# "bbb: tty",
# "tty: ccc",
# "ccc: ddd eee",
# "ddd: hub",
# "hub: fff",
# "eee: dac",
# "dac: fff",
# "fff: ggg hhh",
# "ggg: out",
# "hhh: out",
# ]

class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.outputs: list[Node] = []
        self.parents: list[Node] = []

def parse_input():
    nodes = {}
    for line in ar:
        liner = line.split(" ")
        name = liner[0][:-1]
        outputs = liner[1:]
        if name not in nodes:
            nodes[name] = Node(name)
        for output in outputs:
            if output not in nodes:
                nodes[output] = Node(output)
            nodes[output].parents.append(nodes[name])
            nodes[name].outputs.append(nodes[output])
    return nodes

def part1():
    nodes = parse_input()
    queue = [( (), nodes["you"] )]
    seen = {()}

    total = 0
    while queue:
        path, current = queue.pop()
        if current == nodes["out"]:
            total += 1
        else:
            for next in current.outputs:
                new_path = tuple(list(path) + [next])
                if new_path not in seen or next in path:
                    seen.add(new_path)
                    queue.append((new_path, next))
    print(total)

# part1()


def part2():
    nodes = parse_input()

    @cache
    def dfs(node: Node, target: str) -> int:
        if node == nodes[target]:
            return 1
        else:
            sub_tot = 0
            for next in node.outputs:
                sub_tot += dfs(next, target)
            return sub_tot


    print(dfs(nodes["svr"], "fft") * dfs(nodes["fft"], "dac") * dfs(nodes["dac"], "out"))

part2()
