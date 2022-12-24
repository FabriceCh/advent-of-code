import math
from utils import read_file

ar = read_file("/home/fabrice/advent-of-code/2022/input")

ar2 = [
    "2,18 -2,15", 
    "9,16 10,16", 
    "13,2 15,3", 
    "12,14 10,16", 
    "10,20 10,16", 
    "14,17 10,16", 
    "8,7 2,10", 
    "2,0 2,10", 
    "0,11 2,10", 
    "20,14 25,17", 
    "17,20 21,22", 
    "16,7 15,3", 
    "14,3 15,3", 
    "20,1 15,3", 

]

def man_dist(sensor, pos):
    rel_pos = [abs(pp - ss) for ss, pp in zip(sensor, pos)]
    return sum(rel_pos)

def build_map(ar):
    sensors = {}
    abs_beacs = []
    for line in ar:
        blocks = line.split(" ")
        sens_pos = [int(a) for a in blocks[0].split(",")]
        beac_pos = [int(a) for a in blocks[1].split(",")]
        sensors[tuple(sens_pos)] = {"b": beac_pos, "r": man_dist(sens_pos, beac_pos)}
        abs_beacs.append(tuple(beac_pos))
    return sensors, abs_beacs
    
def merge_pass(intervals):
    for i, ia in enumerate(intervals):
            for j, ib in enumerate(intervals):
                if j != i:
                    if ia[0] >= ib[0] and ia[0] <= ib[1]:
                        intervals.pop(max(i, j))
                        intervals.pop(min(i, j))
                        #print([min(ia[0], ib[0]), max(ia[1], ib[1])])
                        intervals.append([min(ia[0], ib[0]), max(ia[1], ib[1])])
                        return intervals
                    elif ia[1] >= ib[0] and ia[1] <= ib[1]:
                        intervals.pop(max(i, j))
                        intervals.pop(min(i, j))
                        #print([min(ia[0], ib[0]), max(ia[1], ib[1])])
                        intervals.append([min(ia[0], ib[0]), max(ia[1], ib[1])])
                        return intervals
    return intervals

def merge_intervals(intervals):
    changed = True
    #print(intervals)
    while changed:
        old_len = len(intervals)
        intervals = sorted(intervals, key=lambda x: x[0])
        #print(intervals)
        intervals = merge_pass(intervals)
        new_len = len(intervals)
        changed = old_len != new_len
        #print(changed)
    return intervals

def part1():
    sensors, abs_beacs = build_map(ar)
    
    
    lj = 2000000
    lj = 10
    intervals = []
    for s, dd in sensors.items():
        dist_from_line = abs(lj - s[1])
        #print(s)
        #print([s[0] - (sensors[s]["r"] - dist_from_line), s[0] + (sensors[s]["r"] - dist_from_line)])
        if dist_from_line <= sensors[s]["r"]:
            intervals.append([s[0] - (sensors[s]["r"] - dist_from_line), s[0] + (sensors[s]["r"] - dist_from_line)])
    


    
    intervals = merge_intervals(intervals)

    c = 1
    for inter in intervals:
        c += abs(inter[1] - inter[0])
    #print("before beacons:", c)

    for b in set(abs_beacs):
        if b[1] == lj:
            c -= 1
            #print(b)
            continue

    print(c)

def part2():
    sensors, abs_beacs = build_map(ar)
    all_intervals = []
    for cur_i in range(4000000):
    #for cur_i in range(20):
        if cur_i % 100000 == 0:
            print(cur_i)
        intervals = []
        for s in sensors.keys():
            dist_from_line = abs(cur_i - s[1])
            if dist_from_line <= sensors[s]["r"]:
                intervals.append([s[0] - (sensors[s]["r"] - dist_from_line), s[0] + (sensors[s]["r"] - dist_from_line)])
        
        intervals = merge_intervals(intervals)

        if len(intervals) > 1:
            for ind in range(len(intervals)-1):
                if intervals[ind][1] != intervals[ind + 1][0] - 1:

                    xxx = intervals[ind][1] + 1
                    yyy = cur_i
                    print(xxx*4000000 + yyy)
                    return


#part1()
part2()
