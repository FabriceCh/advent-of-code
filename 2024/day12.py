from utils import read_file, Grid

ar = read_file("2024/input")
ar = [
    "RRRRIICCFF",
    "RRRRIICCCF",
    "VVRRRCCFFF",
    "VVRCCCJFFF",
    "VVVVCJJCFE",
    "VVIVCCJJEE",
    "VVIIICJJEE",
    "MIIIIIJJEE",
    "MIIISIJEEE",
    "MMMISSJEEE",
]

grid = Grid(ar)

global_seen = set()
total = 0
total_part2 = 0
for zone_type, x, y in grid:
    if (x, y) in global_seen:
        continue
    area = 0
    perimeter = 0
    corners = 0
    zone_seen = set()
    oob_seen = set()
    stack = [(x, y)]
    while stack:
        current_tile = stack.pop()
        if current_tile in zone_seen:
            continue
        global_seen.add(current_tile)
        zone_seen.add(current_tile)
        area += 1
        edges = 0
        for neighbor in grid.get_neighbors_coords(*current_tile, in_bound_only=False):
            if grid.is_out_of_bounds(*neighbor) or grid.get(*neighbor) != zone_type:
                if neighbor in oob_seen:
                    corners += 1
                perimeter += 1
                edges += 1
                oob_seen.add(neighbor)
            else:
                stack.append(neighbor)
        if edges == 2:
            corners += 1
        elif edges == 3:
            corners += 2
        elif edges == 4:
            corners = 4

    print(f"adding area {area} * {corners} corners")
    print("for zone ", zone_type, zone_seen)
    total += area * perimeter
    total_part2 += area * corners

print(total)
print(total_part2)
