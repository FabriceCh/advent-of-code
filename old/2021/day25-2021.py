def read_file(path):
    arr = []
    with open(path, "r") as file:
        for line in file:
            arr.append(line.rstrip())
    return arr

ar = read_file("input")

####################

_map = []
for line in ar:
    _map.append(list(line))
X_LEN = len(_map[0])
Y_LEN = len(_map)

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Step_executor():
    def __init__(self, _map):
        self._map = _map
        self.right_updates = {}
        self.down_updates = {}

    def access_map(self, pos):
        return self._map[pos.y][pos.x]
    
    def update_map_pos(self, pos, val):
        self._map[pos.y][pos.x] = val

    def pos_wrapper(self, pos: Position):
        x = pos.x
        if pos.x == X_LEN:
            pos.x = 0
        y = pos.y
        if pos.y == Y_LEN:
            pos.y = 0

    def update_right_position(self, pos: Position):
        if self.access_map(pos) == ">":
            pos_to_check = Position(pos.x, pos.y)
            pos_to_check.x += 1
            self.pos_wrapper(pos_to_check)
            if self.access_map(pos_to_check) == ".":
                self.right_updates[pos] = "."
                self.right_updates[pos_to_check] = ">"
    
    def update_down_position(self, pos: Position):
        if self.access_map(pos) == "v":
            pos_to_check = Position(pos.x, pos.y)
            pos_to_check.y += 1
            self.pos_wrapper(pos_to_check)
            if self.access_map(pos_to_check) == ".":
                self.down_updates[pos] = "."
                self.down_updates[pos_to_check] = "v"

    def update_map(self):
        for pos, val in self.right_updates.items():
            self.update_map_pos(pos, val)
        self.right_updates = {}
        for pos, val in self.down_updates.items():
            self.update_map_pos(pos, val)
        self.down_updates = {}


    def execute_step(self) -> bool:
        
        # move rights
        for y_, line in enumerate(_map):
            for x_, _ in enumerate(line):
                self.update_right_position(pos=Position(x_, y_))
        is_rights_moving = bool(self.right_updates)
        self.update_map()

        # move downs
        for y_, line in enumerate(_map):
            for x_, _ in enumerate(line):
                self.update_down_position(pos=Position(x_, y_))
        is_downs_moving = bool(self.down_updates)
        self.update_map()

        # return true if still any update
        return is_downs_moving or is_rights_moving

executor = Step_executor(_map)
is_moving = True
counter = 0

while is_moving:
    is_moving = executor.execute_step()
    counter += 1
    print(counter)

print(counter)