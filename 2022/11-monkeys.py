from aocd import get_data
ar = get_data(day=11, year=2022)
ar = ar.splitlines()

#print(ar)

from utils import read_file

#ar = read_file("/home/fabrice/advent-of-code/2022/test_ex")

#print(ar)
ar.append(" ")


class Monkey:
    def __init__(self, name, starting_items, operation, test, if_true, if_false):
        self.name = name
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.n_processed = 0

    def inspect(self):
        to_give = []
        while self.items:
            item = self.items.pop(0)
            self.n_processed += 1
            if self.operation.split(" ")[1] == "old":
                bb = item
            else:
                bb = int(self.operation.split(" ")[1])
            if self.operation[0] == "*":
                item *= bb
                #is_test_true = (item * bb) % int(self.test) == 0
            if self.operation[0] == "+":
                item += bb
                #is_test_true = ((item) % int(self.test) + (bb) % int(self.test)) % int(self.test)  == 0
                #item += bb
            #item = item // 3

            if (item) % int(self.test) == 0:
                to_give.append([self.if_true, item])
            else:
                to_give.append([self.if_false, item])
        return to_give


def text_to_monkeys(text):
    monks = []
    name, items, op, test, if_true, if_false = "", "", "", "", "", ""
    for l in text:

        
        if l.startswith("Monkey"):
            name = l.split(" ")[1][0]
        elif l.startswith("  Starting items"):
            items = [int(a[:-1]) for a in l.split(" ")[4:-1]] + [int(l.split(" ")[-1])]
        elif l.startswith("  Operation:"):
            op = l[23:]
        elif l.startswith("  Test: "):
            test = l.split(":")[1].split(" ")[3]
        elif l.startswith("    If true:"):
            if_true = l.split(":")[1].split(" ")[4]
        elif l.startswith("    If false:"):
            if_false = l.split(":")[1].split(" ")[4]
        else:
            monks.append(Monkey(name, items, op, test, if_true, if_false))
    return monks

def part1():
    ans = 0
    monks = text_to_monkeys(ar)

    big_mama = 1
    for moo in monks:
        big_mama *= int(moo.test)

    for _ in range(10000):
        for monk in monks:
            #print("monkey", monk.name)
            #print("items after", monk.items)
            to_give = monk.inspect()
            #print(" operation", monk.operation)
            #print("test", monk.test)
            #print("to_give", to_give)
            for mm, it in to_give:
                for m in monks:
                    if m.name == mm:
                        m.items.append(it % int(big_mama))
    ns = []
    for m in monks:
        print(m.n_processed)
        ns.append(m.n_processed)
    ns.sort()
    print(ns[-1] * ns[-2])

part1()