from utils import read_file

ar = read_file("/home/fabrice/advent-of-code/2022/input")


def part1():
    answer = 0
    cycle = 1
    X = 1
    addx = False
    value = 0
    instruction = None

    while cycle < 300:
        if not ar:
            break
        if (cycle - 20) % 40 == 0:
            answer += cycle * X
            print(instruction)
            print(addx)
            print(cycle, X)
        cycle += 1
        if not addx:
            instruction = ar.pop(0)
        else:
            X += int(value)
            addx = False
            
            continue
        if instruction == "noop":
            
            continue
        else:
            value = instruction.split(" ")[1]
            addx = True
        
    print(answer)

#part1()


def is_lit(cycle, X):
    return abs(((cycle - 1) % 40) - X)  <= 1

def part2():
    answer = 0
    cycle = 1
    X = 1
    addx = False
    value = 0
    instruction = None

    CTR = []

    while cycle < 300:
        if not ar:
            break
        if is_lit(cycle, X):
            CTR.append("#")
        else:
            CTR.append(".")
            
        cycle += 1
        if not addx:
            instruction = ar.pop(0)
        else:
            X += int(value)
            addx = False
            
            continue
        if instruction == "noop":
            
            continue
        else:
            value = instruction.split(" ")[1]
            addx = True
        
    print("".join(CTR[0:40]))
    print("".join(CTR[40:80]))
    print("".join(CTR[80:120]))
    print("".join(CTR[120:160]))
    print("".join(CTR[160:200]))
    print("".join(CTR[200:240]))

part2()