from advent.utils.utils import printer, read_file
import copy
from scipy.optimize import linprog


ar = read_file("input")
# ar = [
# "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
# "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
# "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
# ]

class Machine:
    def __init__(self, line: str):
        liner = [e for e in line.split(" ")]
        self.state: str = liner[0][1:-1]
        buttons = liner[1:-1]
        buttons = [b[1:-1].split(",") for b in buttons]
        self.buttons = [[int(d) for d in b] for b in buttons]
        self.voltages = [int(d) for d in liner[-1][1:-1].split(",")]



machines = []
for line in ar:
    new_machine = Machine(line)
    machines.append(new_machine)
    # print(new_machine.state, new_machine.buttons, new_machine.voltages)

def part2():
    total = 0
    for m in machines:
        c  = [1 for _ in m.buttons]
        A_matrix = [[i in b for b in m.buttons] for i in range(len(m.voltages))]
        total += linprog(c, A_eq=A_matrix, b_eq=m.voltages, integrality=1).fun
    print(int(total))

part2()

def press(button, state):
    new_state = [c for c in copy.copy(state)]
    for i in button:
        new_state[i] = '#' if new_state[i] == '.' else '.'
    return "".join(new_state)

def find_min_presses(m: Machine):
    state = "."*len(m.state)
    seen = { state }
    queue = [(state, 0)]
    while True:
        state, n_press = queue.pop(0)
        n_press += 1
        for b in m.buttons:
            new_state = press(b, state)
            if new_state == m.state:
                return n_press
            else:
                if new_state not in seen:
                    queue.append((new_state, n_press))
                    seen.add(new_state)

def part1():
    total = 0
    for i, m in enumerate(machines):
        min_press = find_min_presses(m)
        total += min_press
    return total




    
