from collections.abc import Sequence
from typing import Callable, Tuple
import functools


def read_file(path="input.txt") -> list[str]:
    """
    Basic function to read file content
    """
    arr = []
    with open(path, "r") as file:
        for line in file:
            arr.append(line.rstrip())
    return arr


def count_occurences(input_list: list) -> dict:
    """
    Transform a list into a dictionary of counts of each element from the list
    """
    occurences = {}
    for element in input_list:
        if element not in occurences:
            occurences[element] = 1
        else:
            occurences[element] += 1
    return occurences

def printer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Call the original function
        print(result)
        return result
    return wrapper

def merge_intervals(intervals: list[Tuple[int, int]]) -> list[Tuple[int, int]]:
    intervals.sort(key=lambda x: x[0])
    i = 0
    new_intervals = [intervals.pop(0)]
    for interval in intervals:
        ramin, ramax = new_intervals[-1][0], new_intervals[-1][1]
        rbmin, rbmax = interval[0], interval[1]
        if  rbmin >= ramin and rbmin <= ramax:
            new_r = (ramin, max(ramax, rbmax))
            new_intervals.pop()
            new_intervals.append(new_r)
        else:
            new_intervals.append(intervals[i])
        i += 1
    return new_intervals



class Grid:
    """
    2D grid-like operations
    """

    def __init__(self, gridLike: Sequence[str | list], nesw_map=["^", ">", "v", "<"]):
        self._height = len(gridLike)
        self._width = len(gridLike[0])
        self._grid = self.convert_list_str_to_list_list(gridLike)
        self._nesw_map = nesw_map

    def convert_list_str_to_list_list(
        self, list_in: Sequence[str | list]
    ) -> list[list]:
        return [[char for char in line] for line in list_in]

    def __str__(self):
        return "\n".join("".join(map(str, sl)) for sl in self._grid)

    def __iter__(self):
        self._x_iter = 0
        self._y_iter = 0
        return self

    def __next__(self):
        x, y = self._x_iter, self._y_iter
        if y == self._height or x == self._width:
            raise StopIteration
        value = self.get(x, y)
        if self._x_iter < self._width - 1:
            self._x_iter += 1
        else:
            self._x_iter = 0
            self._y_iter += 1
        return value, x, y

    def cast_to_int(self):
        """
        Cast every element of the grid to int()
        """
        self._grid = [[int(char) for char in line] for line in self._grid]

    def is_x_out_of_bounds(self, x):
        return x < 0 or x >= self._width

    def is_y_out_of_bounds(self, y):
        return y < 0 or y >= self._height

    def is_out_of_bounds(self, x, y):
        return self.is_x_out_of_bounds(x) or self.is_y_out_of_bounds(y)

    def set(self, x: int, y: int, value):
        if self.is_out_of_bounds(x, y):
            print("x:", x, "y:", y)
            raise IndexError
        self._grid[y][x] = value

    def get(self, x: int, y: int):
        """
        Get the value at (x, y)
        """
        if x < 0 or y < 0:
            raise IndexError
        return self._grid[y][x]

    def get_south(self, x: int, y: int):
        return self.get(x, y + 1)

    def get_north(self, x: int, y: int):
        return self.get(x, y - 1)

    def get_west(self, x: int, y: int):
        return self.get(x - 1, y)

    def get_east(self, x: int, y: int):
        return self.get(x + 1, y)

    # get coordinates of neighbors
    def get_south_coord(self, x: int, y: int) -> tuple[int, int]:
        return (x, y + 1)

    def get_north_coord(self, x: int, y: int) -> tuple[int, int]:
        return (x, y - 1)

    def get_west_coord(self, x: int, y: int) -> tuple[int, int]:
        return (x - 1, y)

    def get_east_coord(self, x: int, y: int) -> tuple[int, int]:
        return (x + 1, y)

    def get_south_east_coord(self, x: int, y: int) -> tuple[int, int]:
        return (x + 1, y + 1)

    def get_south_west_coord(self, x: int, y: int) -> tuple[int, int]:
        return (x - 1, y + 1)

    def get_north_east_coord(self, x: int, y: int) -> tuple[int, int]:
        return (x + 1, y - 1)

    def get_north_west_coord(self, x: int, y: int) -> tuple[int, int]:
        return (x - 1, y - 1)

    def get_direction_coord_fun(
        self, direction_char: str
    ) -> Callable[[int, int], tuple[int, int]]:
        if direction_char == self._nesw_map[0]:
            return self.get_north_coord
        elif direction_char == self._nesw_map[1]:
            return self.get_east_coord
        elif direction_char == self._nesw_map[2]:
            return self.get_south_coord
        elif direction_char == self._nesw_map[3]:
            return self.get_west_coord
        raise (
            Exception(
                f"direction_char must be a direction in this map: {self._nesw_map}"
            )
        )

    def list_get_coordinates_functions(
        self, enable_diag=True
    ) -> list[Callable[[int, int], tuple[int, int]]]:
        functions = [
            self.get_south_coord,
            self.get_north_coord,
            self.get_west_coord,
            self.get_east_coord,
        ]
        if enable_diag:
            functions += [
                self.get_north_west_coord,
                self.get_north_east_coord,
                self.get_south_east_coord,
                self.get_south_west_coord,
            ]
        return functions

    def get_full_neighbors_info(self, x, y, in_bound_only=True):
        info = []

        def add_to_info(neigh_coords, dir):
            if in_bound_only:
                if self.is_out_of_bounds(*neigh_coords):
                    return
            info.append(
                {
                    "dir": dir,
                    "val": self.get(*neigh_coords),
                    "pos": neigh_coords,
                }
            )

        add_to_info(self.get_north_coord(x, y), self._nesw_map[0])
        add_to_info(self.get_east_coord(x, y), self._nesw_map[1])
        add_to_info(self.get_south_coord(x, y), self._nesw_map[2])
        add_to_info(self.get_west_coord(x, y), self._nesw_map[3])
        return info

    def get_neighbors_coords(
        self, x, y, enable_diag=False, in_bound_only=True
    ) -> list[tuple[int, int]]:
        coord_funcs = self.list_get_coordinates_functions(enable_diag)
        coords = [coord_f(x, y) for coord_f in coord_funcs]
        if in_bound_only:
            coords = [
                coord
                for coord in coords
                if not self.is_out_of_bounds(coord[0], coord[1])
            ]
        return coords

    def get_next_n(
        self,
        x: int,
        y: int,
        get_direction_coord: Callable[[int, int], tuple[int, int]],
        n: int | None = None,
        include_start=False,
    ):
        result = []
        if include_start:
            result.append(self.get(x, y))
        if n is None:
            n = max(self._width, self._height)
        for _ in range(n):
            x, y = get_direction_coord(x, y)
            if self.is_out_of_bounds(x, y):
                break
            result.append(self.get(x, y))
        return result

    def set_next_n(
        self,
        x: int,
        y: int,
        values: list,
        get_direction_coord: Callable[[int, int], tuple[int, int]],
        include_start=False,
    ):
        if not include_start:
            x, y = get_direction_coord(x, y)
        for item in values:
            self.set(x, y, item)
            x, y = get_direction_coord(x, y)
            if self.is_out_of_bounds(x, y):
                break

    def shift_next_n(
        self,
        x: int,
        y: int,
        get_direction_coord: Callable[[int, int], tuple[int, int]],
        n: int | None = None,
        include_start=False,
    ):
        shifted = self.get_next_n(x, y, get_direction_coord, n, include_start)
        shifted.insert(0, shifted.pop())
        self.set_next_n(x, y, shifted, get_direction_coord, include_start)

    def get_next_n_right(self, y, x, n=-1, include_start=False):
        """
        Get n right values from (x,y)
        """
        if n == -1:
            n = self._width
        result = []
        i = 0
        if include_start:
            i = -1
        while i < n and not self.is_x_out_of_bounds(x):
            i += 1
            result.append(self.get(x + i, y))
        return result


if __name__ == "__main__":
    # reserved for testing
    grid = Grid([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
    n_coords = grid.get_neighbors_coords(1, 0)
    print(n_coords)
