from advent.utils.utils import read_file


ar = read_file()
# ar = [
#     "Register A: 729",
#     "Register B: 0",
#     "Register C: 0",
#     "",
#     "Program: 0,1,5,4,3,0",
# ]


class Computer:
    def __init__(self, ar):
        self.a = 0
        self.b = 0
        self.c = 0
        self.program = ""
        self.instruction_pointer = 0
        self.outputs = []

        for line in ar:
            if "A" in line:
                self.a = int(line.split(" ")[-1])
            if "B" in line:
                self.b = int(line.split(" ")[-1])
            if "C" in line:
                self.c = int(line.split(" ")[-1])
            if "Program" in line:
                self.program = line.split(" ")[-1].replace(",", "")
                break

    def print_current_state(self):
        print("register A:", self.a)
        print("register B:", self.b)
        print("register C:", self.c)

    def increment_instruction_pointer(self):
        self.instruction_pointer += 2

    def execute_program(self):
        while self.instruction_pointer < len(self.program):
            self.print_current_state()
            opcode = int(self.program[self.instruction_pointer])
            operand = int(self.program[self.instruction_pointer + 1])
            instruction = self.opcode_to_function(opcode)
            instruction(operand)
        output: str = ",".join([str(o) for o in self.outputs])
        print(output)

    def combo(self, operand):
        if operand < 4:
            return operand
        elif operand == 4:
            return self.a
        elif operand == 5:
            return self.b
        elif operand == 6:
            return self.c
        else:
            raise Exception("invalid operand: program is not valid")

    def opcode_to_function(self, opcode):
        INSTRUCTIONS_FUNCTIONS = [
            self.adv,
            self.bxl,
            self.bst,
            self.jnz,
            self.bxc,
            self.out,
            self.bdv,
            self.cdv,
        ]
        return INSTRUCTIONS_FUNCTIONS[opcode]

    def adv(self, operand):  # 0
        self.increment_instruction_pointer()
        result = self.a // (2 ** self.combo(operand))
        self.a = result

    def bxl(self, operand):  # 1
        self.increment_instruction_pointer()
        result = self.b ^ operand
        self.b = result

    def bst(self, operand):  # 2
        self.increment_instruction_pointer()
        result = self.combo(operand) % 8
        self.b = result

    def jnz(self, operand):  # 3
        if self.a == 0:
            self.increment_instruction_pointer()
            return
        self.instruction_pointer = operand

    def bxc(self, _):  # 4
        self.increment_instruction_pointer()
        result = self.b ^ self.c
        self.b = result

    def out(self, operand):  # 5
        self.increment_instruction_pointer()
        result = self.combo(operand) % 8
        self.outputs.append(result)

    def bdv(self, operand):  # 6
        self.increment_instruction_pointer()
        result = self.a // (2 ** self.combo(operand))
        self.b = result

    def cdv(self, operand):  # 7
        self.increment_instruction_pointer()
        result = self.a // (2 ** self.combo(operand))
        self.c = result


computer = Computer(ar)
computer.execute_program()
computer.print_current_state()
