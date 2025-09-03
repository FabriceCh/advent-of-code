import typing


def read_file(path):
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


class Grid:
    """
    2D grid-like operations
    """

    def __init__(self, gridLike: list[list]):
        self.height = len(gridLike)
        self.width = len(gridLike[0])
        self.grid = gridLike

    def __str__(self):
        return "\n".join(" ".join(map(str, sl)) for sl in self.grid)

    def __iter__(self):
        self.x_iter = 0
        self.y_iter = 0
        return self

    def __next__(self):
        x, y = self.x_iter, self.y_iter
        if y == self.height or x == self.width:
            raise StopIteration
        value = self.get(x, y)
        if self.x_iter < self.width - 1:
            self.x_iter += 1
        else:
            self.x_iter = 0
            self.y_iter += 1
        return value, x, y

    def is_x_out_of_bounds(self, x):
        return x < 0 or x >= self.width

    def is_y_out_of_bounds(self, y):
        return y < 0 or y >= self.height

    def is_out_of_bounds(self, x, y):
        return self.is_x_out_of_bounds(x) or self.is_y_out_of_bounds(y)

    # get the value out of a position
    def get(self, x, y):
        if x < 0 or y < 0:
            raise IndexError
        return self.grid[y][x]

    def get_south(self, x, y):
        return self.get(x, y + 1)

    def get_north(self, x, y):
        return self.get(x, y - 1)

    def get_west(self, x, y):
        return self.get(x - 1, y)

    def get_east(self, x, y):
        return self.get(x + 1, y)

    # get coordinates of neighbors
    def get_south_coord(self, x, y):
        return (x, y + 1)

    def get_north_coord(self, x, y):
        return (x, y - 1)

    def get_west_coord(self, x, y):
        return (x - 1, y)

    def get_east_coord(self, x, y):
        return (x + 1, y)

    def get_south_east_coord(self, x, y):
        return (x + 1, y + 1)

    def get_south_west_coord(self, x, y):
        return (x - 1, y + 1)

    def get_north_east_coord(self, x, y):
        return (x + 1, y - 1)

    def get_north_west_coord(self, x, y):
        return (x - 1, y - 1)

    def list_get_coordinates_functions(self, enable_diag=True):
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

    def get_next_n(
        self,
        x: int,
        y: int,
        get_direction_coord: typing.Callable[[int, int], tuple[int, int]],
        n: int | None = None,
    ):
        result = []
        if n is None:
            n = max(self.width, self.height)
        for _ in range(n):
            x, y = get_direction_coord(x, y)
            if self.is_out_of_bounds(x, y):
                break
            result.append(self.get(x, y))
        return result

    def get_next_n_right(self, y, x, n=-1):
        """
        Get n right values from (x,y)
        """
        if n == -1:
            n = self.width
        result = []
        i = 0
        while i < n and not self.is_x_out_of_bounds(x):
            i += 1
            result.append(self.get(x + i, y))
        return result


if __name__ == "__main__":
    # space reserved for testing
    arr = [1, 2, 23, 4, "adgf", 1, 1, 1]
    [print(a) for a in arr]
    print(count_occurences(arr))
