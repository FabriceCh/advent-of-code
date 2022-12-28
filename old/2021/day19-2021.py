from typing import List
import math

def read_file(path):
    arr = []
    with open(path, "r") as file:
        for line in file:
            arr.append(line.rstrip())
    return arr

ar = read_file("test19")
#ar = read_file("input19")


class Scanner:
    def __init__(self, name, raw_beacons):
        self.name = name
        self.positions = self._raw_to_positions(raw_beacons)
        self.distances = self._get_rel_distances(self.positions)

    def _raw_to_positions(self, raw_beacons):
        positions = []
        for line in raw_beacons:
            if line == "":
                continue
            positions.append([int(a) for a in line.split(",")])
        return positions

    def _get_rel_distances(self, positions):
        distances = {i: [] for i in range(len(positions))}
        for i, pos in enumerate(positions):
            for j, pos2 in enumerate(positions):
                if j != i:
                    dist = (pos[0]-pos2[0])**2 + (pos[1]-pos2[1])**2 + (pos[2]-pos2[2])**2
                    distances[i].append(dist)
            distances[i].sort()
        return distances


scanners_delmiters = []
for i, line in enumerate(ar):
    if "scanner" in line:
        scanners_delmiters.append(i)
scanners: List[Scanner] = []
for j, scanner_i in enumerate(scanners_delmiters):
    if j < len(scanners_delmiters) - 1:
        scanners.append(Scanner(ar[scanner_i], ar[scanner_i+1:scanners_delmiters[j+1]]))
    else:
        scanners.append(Scanner(ar[scanner_i], ar[scanner_i+1:]))

all_distances = [d for s in scanners for d in s.distances]

duplicates = []
seen = {}
for i, s in enumerate(scanners):
    for s2 in scanners[i:]:
        if s.name != s2.name:
            print("comparing", s.name, "with", s2.name)
            scanner_dups = []

            for dist in s.distances.values():
                for dist2 in s2.distances.values():
                    n_sim_dist = 0
                    for d in dist:
                        if d in dist2:
                            n_sim_dist += 1
                    if n_sim_dist >= 1:
                        scanner_dups.append(tuple(dist))
                        continue
                
            print(len(scanner_dups))
            if len(scanner_dups) >= 12:
                duplicates += scanner_dups

print(len(all_distances) - len(set(duplicates)))
