from aocd import get_data
ar = get_data(day=9, year=2022)
ar = ar.splitlines()

def update_head(head, dir):
    if dir == "U":
        head[1] += 1
    elif dir == "D":
        head[1] -= 1
    elif dir == "R":
        head[0] += 1
    elif dir == "L":
        head[0] -= 1

def is_tail_next_to_head(tail, head):
    return (abs(tail[0] - head[0]) < 2 and abs(tail[1] - head[1]) < 2)

def is_tail_same_row_or_column(tail, head):
    return (tail[0] == head[0] or tail[1] == head[1])

def update_tail_straight(tail, head):
    if head[0] == tail[0]:
        if head[1] > tail[1]:
            tail[1] += 1
        elif head[1] < tail[1]:
            tail[1] -= 1
        return
    if head[1] == tail[1]:
        if head[0] > tail[0]:
            tail[0] += 1
        elif head[0] < tail[0]:
            tail[0] -= 1

def update_tail_diag(tail, head):
    if head[0] > tail[0]:
        tail[0] += 1
    elif head[0] < tail[0]:
        tail[0] -= 1
    if head[1] > tail[1]:
        tail[1] += 1
    elif head[1] < tail[1]:
        tail[1] -= 1

def update_tail(tail, head):
    if is_tail_next_to_head(tail, head):
        return
    if is_tail_same_row_or_column(tail, head):
        update_tail_straight(tail, head)
    else:
        update_tail_diag(tail, head)
    

def exec_step(line, tail, head):
    dir = line[0]
    update_head(head, dir)
    update_tail(tail, head)

def exec_step2(line, tails, head):
    dir = line[0]
    update_head(head, dir)
    for i in range(9):
        if i == 0:
            update_tail(tails[i], head)
        else:
            update_tail(tails[i], tails[i-1])

def part1(ar):
    visited = {(0,0)}
    head = [0,0]
    tail = [0,0]
    for line in ar:
        n_steps = line.split(" ")[1]
        for _ in range(int(n_steps)):
            exec_step(line, tail, head)
            visited.add(tuple(tail))
    print(len(visited))


def part2(ar):
    visited = {(0,0)}
    head = [0,0]
    tails = [[0,0] for i in range(9)]
    for line in ar:
        n_steps = line.split(" ")[1]
        for _ in range(int(n_steps)):
            exec_step2(line, tails, head)
            visited.add(tuple(tails[8]))
    print(len(visited))

part1(ar)
part2(ar)
