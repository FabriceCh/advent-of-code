from utils import read_file

lines = read_file("/home/fabrice/advent-of-code/2022/input")
lines2 = [
    "root: pppw + sjmn",
    "pppw: cczh / lfqf",
    "cczh: sllz + lgvd",
    "sjmn: drzm * dbpl",
    "ptdq: humn - dvpt",
    "drzm: hmdt - zczc",
    "lgvd: ljgn * ptdq",
    "dbpl: 5",
    "zczc: 2",
    "dvpt: 3",
    "lfqf: 4",
    "humn: 5",
    "ljgn: 2",
    "sllz: 4",
    "hmdt: 32",
]

def in_to_dict(lines):
    nodes = {}
    for l in lines:
        key, op = l.split(":")
        op = op.split(" ")[1:]
        nodes[key] = op
    return nodes

def get_val_from_node(name, nodes):
    if name == "humn":
        return []
    if len(nodes[name]) == 3:
        n1, n2 = nodes[name][0], nodes[name][2]
        left, right = get_val_from_node(n1, nodes), get_val_from_node(n2, nodes)
        rev = False
        if isinstance(right, list):
            left, right = right, left
            rev = True
        if isinstance(left, list):
            #print(left, [(nodes[name][1], right)])
            op = (nodes[name][1], right)
            if rev:
                op = (f"{nodes[name][1]}{nodes[name][1]}", right)
            return left + [op]
        if nodes[name][1] == "+":
            return left + right
        if nodes[name][1] == "-":
            return left - right
        if nodes[name][1] == "*":
            return left * right
        if nodes[name][1] == "/":
            return int(left / right)
    elif len(nodes[name]) == 1:
        return int(nodes[name][0])

def get_val_from_node_with_ans(name, nodes, humn_val):
    if name == "humn":
        return humn_val
    if len(nodes[name]) == 3:
        n1, n2 = nodes[name][0], nodes[name][2]
        left, right = get_val_from_node_with_ans(n1, nodes, humn_val), get_val_from_node_with_ans(n2, nodes, humn_val)

        if nodes[name][1] == "+":
            return left + right
        if nodes[name][1] == "-":
            return left - right
        if nodes[name][1] == "*":
            return left * right
        if nodes[name][1] == "/":
            return int(left / right)
    elif len(nodes[name]) == 1:
        return int(nodes[name][0])


def part1(original = False, answer=5):

    
    nodes = in_to_dict(lines)
    root = "root"
    if original and answer != 5:
        answer = 585
    if answer == 5 or answer == 585:
        print("original part1 answer:")
        print(get_val_from_node_with_ans(root, nodes, answer))
    else:
        n1, n2 = nodes[root][0], nodes[root][2]
        v1 = get_val_from_node_with_ans(n1, nodes, answer)
        v2 = get_val_from_node_with_ans(n2, nodes, answer)
        print(v1)
        print(v2)



def part2():
    nodes = in_to_dict(lines)
    root = "root"
    n1, n2 = nodes[root][0], nodes[root][2]
    v1 = get_val_from_node(n1, nodes)
    v2 = get_val_from_node(n2, nodes)
    if isinstance(v2, list):
        v1, v2 = v2, v1
    print(v1)
    print(v2)
    real_eq = f"({v2})"
    if isinstance(v1, list):
        ans = v2
        while v1:
            cur_op = v1.pop()
            if cur_op[0] == "+" or cur_op[0] == "++":
                ans -= cur_op[1]
                real_eq = f"({real_eq}-{cur_op[1]})"
            if cur_op[0] == "-":
                ans += cur_op[1]
                real_eq = f"({real_eq}+{cur_op[1]})"
            if cur_op[0] == "*" or cur_op[0] == "**":
                ans /= cur_op[1]
                real_eq = f"({real_eq}/{cur_op[1]})"
            if cur_op[0] == "/":
                ans *= cur_op[1]
                real_eq = f"({real_eq}*{cur_op[1]})"

            if cur_op[0] == "--":
                ans = cur_op[1] - ans
            if cur_op[0] == "//":
                ans = cur_op[1] / ans
            
            print(ans, cur_op)
        print("----ans---")
        print(ans)
        print("---------")
        part1(original = False, answer=ans)
        print(real_eq)
#part1(original=True, answer = 585)
part2()
