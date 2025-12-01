from advent.utils.utils import read_file, Grid

ar = read_file("input.txt")
# ar = [
#     "OOOOO",
#     "OXOOO",
#     "OOXOO",
#     "OOOOO",
# ]

grid = Grid(ar)


def count_interior_corner(x: int, y: int, zone_seen):
    corners = 0
    if (
        (x + 1, y - 1) in zone_seen
        and (x, y - 1) in zone_seen
        and (x + 1, y) in zone_seen
    ):
        corners += 1
    if (
        (x + 1, y + 1) in zone_seen
        and (x, y + 1) in zone_seen
        and (x + 1, y) in zone_seen
    ):
        corners += 1
    if (
        (x - 1, y + 1) in zone_seen
        and (x, y + 1) in zone_seen
        and (x - 1, y) in zone_seen
    ):
        corners += 1
    if (
        (x - 1, y - 1) in zone_seen
        and (x, y - 1) in zone_seen
        and (x - 1, y) in zone_seen
    ):
        corners += 1

    return corners


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
    outer_zone = set()
    seen_outer = set()
    stack = [(x, y)]
    while stack:
        current_tile = stack.pop()
        if current_tile in zone_seen:
            continue
        global_seen.add(current_tile)
        zone_seen.add(current_tile)
        area += 1
        edges = 0
        processed_neighbors = []
        for neighbor in grid.get_neighbors_coords(*current_tile, in_bound_only=False):
            if grid.is_out_of_bounds(*neighbor) or grid.get(*neighbor) != zone_type:
                processed_neighbors.append(neighbor)
                outer_zone.add(neighbor)
                perimeter += 1
                edges += 1
            else:
                if neighbor not in zone_seen:
                    stack.append(neighbor)
        if edges == 2 and (
            processed_neighbors[0][0] != processed_neighbors[1][0]
            and processed_neighbors[0][1] != processed_neighbors[1][1]
        ):
            corners += 1
        elif edges == 3:
            corners += 2
        elif edges == 4:
            corners = 4
    interior_corners = 0
    for outer_tile in outer_zone:
        if outer_tile not in seen_outer:
            current_interior_corners = count_interior_corner(
                outer_tile[0], outer_tile[1], zone_seen
            )
            interior_corners += current_interior_corners
            seen_outer.add(outer_tile)
    corners += interior_corners

    total += area * perimeter
    total_part2 += area * corners
    print(f"zone {zone_type}: area {area} * {corners} corners = {area * corners}")

print(total)
print(total_part2)
