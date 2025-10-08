from __future__ import annotations
from utils import read_file


ar = read_file("2024/input")
line = ar[0]
# line = "2333133121414131402"

free_space = []
blocks = []

for i, digit in enumerate([int(number) for number in line]):
    if (i % 2) == 0:  # block
        blocks.append(digit)
    else:  # free space
        free_space.append(digit)

# part 1
block_index = len(blocks) - 1
free_index = 0
i = blocks[0]
total = 0

block = 0
free = 0


class Meta:
    def __init__(self):
        self.disk = []

    def add_to_total(self, block_index, total, i):
        # self.disk.append()
        total += i * block_index
        i += 1
        return total, i


meta = Meta()


block += blocks[block_index]
free += free_space[free_index]
while free_index < block_index:
    # fill free space
    if free > block:
        for _ in range(block):
            total, i = meta.add_to_total(block_index, total, i)
        free -= block
        block = 0
    else:  # just enough or too much block for current free space
        for _ in range(free):
            total, i = meta.add_to_total(block_index, total, i)
        block -= free
        free = 0
        # add in next original block
        if free_index + 1 < block_index:
            for _ in range(blocks[free_index + 1]):
                total, i = meta.add_to_total(free_index + 1, total, i)
        else:
            for _ in range(block):
                total, i = meta.add_to_total(free_index + 1, total, i)

    # get next if needed
    if block < 1:
        block_index -= 1
        block += blocks[block_index]
    if free < 1:
        free_index += 1
        free += free_space[free_index]


print(total)


# part 2


class Block:
    def __init__(self, size=0, value=0, previous=None, next=None, free=False):
        self.value = value
        self.size = size
        self.previous = previous
        self.next = next
        self.free = free
        self.moved = False

    def is_free(self):
        return self.free


class Disk:
    def __init__(self, data):
        self.start = Block(0)
        self.end = Block(0)
        self.construct_from_raw_data(data)

    def construct_from_raw_data(self, line):
        cur_block = self.start
        for i, digit in enumerate([int(number) for number in line]):
            if (i % 2) == 0:  # block
                new_block = Block(size=digit, value=i // 2, previous=cur_block)
                cur_block.next = new_block
                cur_block = new_block
            else:  # free space
                new_block = Block(size=digit, value=0, previous=cur_block, free=True)
                cur_block.next = new_block
                cur_block = new_block
        self.end = cur_block

    def show_disk(self, reverse=False):
        data = ""
        if reverse:
            cur = self.end
        else:
            cur = self.start
        while cur is not None:
            symb = cur.value
            if cur.is_free():
                symb = "."
            data += "".join([str(symb) for _ in range(cur.size)])
            if reverse:
                cur = cur.previous
            else:
                cur = cur.next
        print(data)

    def insert(self, first_block, second_block, new_block):
        new_block.previous = first_block
        new_block.next = second_block
        first_block.next = new_block
        second_block.previous = new_block

    def find_available_space(self, requested_block):
        cur = self.start
        while cur is not None:
            if cur == requested_block:
                return None
            if cur.is_free() and cur.size >= requested_block.size:
                return cur
            cur = cur.next
        return None

    def compact(self):
        cur_to_move: Block = self.end
        while cur_to_move.previous is not None:
            if cur_to_move.is_free() or cur_to_move.moved:
                cur_to_move = cur_to_move.previous
                continue

            available_space = self.find_available_space(cur_to_move)
            if available_space is not None:
                next_marker = cur_to_move.previous
                available_space.size -= cur_to_move.size
                new_free_block = Block(
                    size=cur_to_move.size,
                    value=0,
                    previous=next_marker,
                    next=cur_to_move.next,
                    free=True,
                )
                next_marker.next = new_free_block
                if cur_to_move.next is not None:
                    cur_to_move.next.previous = new_free_block

                self.insert(available_space.previous, available_space, cur_to_move)
                cur_to_move.moved = True
                cur_to_move = next_marker
            else:
                cur_to_move = cur_to_move.previous
        return

    def checksum(self):
        index = 0
        total = 0
        cur = self.start
        while cur is not None:
            if not cur.is_free():
                for _ in range(cur.size):
                    total += index * cur.value
                    index += 1
            else:
                index += cur.size
            cur = cur.next
        return total


disk = Disk(line)
# disk.show_disk()
# print("00...111...2...333.44.5555.6666.777.888899 (expected)")
disk.compact()
sum = disk.checksum()
# disk.show_disk()
# print("00992111777.44.333....5555.6666.....8888.. (expected)")
print(sum)
