import heapq
import copy
from utils import read_file

ar = read_file("/home/fabrice/advent-of-code/2022/input")

ar2 = [
    "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB",
    "Valve BB has flow rate=13; tunnels lead to valves CC, AA",
    "Valve CC has flow rate=2; tunnels lead to valves DD, BB",
    "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE",
    "Valve EE has flow rate=3; tunnels lead to valves FF, DD",
    "Valve FF has flow rate=0; tunnels lead to valves EE, GG",
    "Valve GG has flow rate=0; tunnels lead to valves FF, HH",
    "Valve HH has flow rate=22; tunnel leads to valve GG",
    "Valve II has flow rate=0; tunnels lead to valves AA, JJ",
    "Valve JJ has flow rate=21; tunnel leads to valve II",
]

def lines_to_valves(lines):
    valves = {}
    for l in lines:
        v_name = l.split(" ")[1]
        v_rate = int(l.split(" ")[4].split("=")[1].split(";")[0])
        next_vs = [a[:2] for a in l.split(" ")[9:]]
        valves[v_name] = {"r": v_rate, "next_vs": next_vs}
    return valves

def find_positive_valves(valves):
    positive_valves = []
    for key, val in valves.items():
        if val["r"] > 0:
            positive_valves.append(key)
    return positive_valves

def dijkstra(valves, start, pos_valves):
    distances = {start: 0}
    seen = {start}
    nodes_to_visit = [(0, start)]

    heapq.heapify(nodes_to_visit)

    while nodes_to_visit:
        cur_node = heapq.heappop(nodes_to_visit)

        if cur_node[1] in pos_valves:
            distances[cur_node[1]] = cur_node[0]

        adjs = valves[cur_node[1]]["next_vs"]
        for adj in adjs:
            if adj not in seen:
                seen.add(adj)
                heapq.heappush(nodes_to_visit, ((cur_node[0] + 1), adj))
    
    return {k: v for k, v in distances.items() if k in pos_valves}

def get_next_possible_valves(sol, all_dists):
    next_valves = []
    remaining_time = 30 - sol["time"] + 1
    #remaining_time = 30 - sol["time"]
    remaining_time = 30 - sol["time"] - 1
    for v in sol["unseen"]:
        if all_dists[sol["current"]][v] < remaining_time and v != sol["current"]:
            next_valves.append(v)
    return next_valves


def update_sol_open_valve(sol, valves):
    new_sol = copy.deepcopy(sol)
    new_sol["time"] += 1
    new_sol["score"] += new_sol["flow"]
    new_sol["flow"] += valves[new_sol["current"]]["r"]
    new_sol["opened"] += [new_sol["current"]]
    new_sol["unseen"].remove(new_sol["current"])
    return new_sol

def part1():
    valves = lines_to_valves(ar)
    pos_valves = find_positive_valves(valves)

    all_dists = {"AA": dijkstra(valves, "AA", pos_valves)}
    for pp in pos_valves:
        all_dists[pp] = dijkstra(valves, pp, pos_valves)

    unseen = copy.deepcopy(pos_valves)
    opened = []
    start = "AA"
    time = 0
    score = 0
    solutions = [{"unseen": unseen, "opened": opened, "current": start, "time": time, "score": score, "flow": 0}]

    big_max = 0

    while solutions:
        sol111 = solutions.pop()
        sol = copy.deepcopy(sol111)

        if sol["time"] > 30:
            print("wtf time exceeded shoudnt happen")
            break
        next_valves = get_next_possible_valves(sol, all_dists)

        # all valves are already opened or no reachable valve until end
        if len(next_valves) == 0:
            # if current valve hasnt been opened, open it
            new_sol = copy.deepcopy(sol)
            if new_sol["current"] not in new_sol["opened"] and new_sol["current"] in new_sol["unseen"]:
                new_sol = update_sol_open_valve(new_sol, valves)
            # compute end of game score
            remaining_time = 30 - new_sol["time"]
            final_score = new_sol["score"] + new_sol["flow"] * remaining_time
            #print(sol)
            if final_score > big_max:
                big_max = final_score
                print(final_score)
                print(new_sol)
        
        else:
            if sol["current"] != "AA":
                new_sol = update_sol_open_valve(sol, valves)
                next_valves = get_next_possible_valves(sol, all_dists)

                for nv in next_valves:
                    dist = all_dists[sol["current"]][nv]
                    sol_to_push = copy.deepcopy(new_sol)
                    sol_to_push["time"] += dist
                    sol_to_push["score"] += (new_sol["flow"] * dist)
                    sol_to_push["current"] = nv
                    solutions.append(sol_to_push)
            else:
                for nv in next_valves:
                    first_sol = copy.deepcopy(sol)
                    first_sol["time"] = sol["time"] + all_dists[sol["current"]][nv]
                    first_sol["current"] = nv
                    solutions.append(first_sol)
    print(big_max)

part1()