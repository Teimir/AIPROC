from datetime import datetime
import time
from typing import List
import os



class Processor:
    def __init__(self):
        self.tc = 0
        self.registers = [0] * 10
        self.pointer = 0
        self.stack = []
        self.instructions = {
            'LDR': self.load,
            'ADD': self.add,
            'SUB': self.subtract,
            'MOV': self.move,
            'POP': self.pop,
            'PUSH': self.push,
            'JMP': self.jump,
            'JFZ': self.jump_if_zero,
            'JFO': self.jump_if_one,
            "PRT": self.print_reg,
            "HALT": self.halt,
            "CMP": self.cmp,
            "GTF": self.get_flag,
        }
        self.labels = {}
        self.data_references = {}
        self.bus = [0] * 256
        # Массив для хранения данных, размером 256 ячеек
        self.ram = [0] * 256
        self.flags = [0, 0, 0, 0, 0, 0, 0, 0]
        #CF - Carry flag ZF - Zero flag SF - Sign flag OF - Overflow flag IE - Interrupt enable flag TF - Trap flag, BL - BiggerLess, EL - Equal

    def in_(self, register1, register2):
        self.registers[int(register2)] = self.bus[self.registers[int(register1)]]

    def out(self, register1, register2):
        self.bus[self.registers[int(register1)]] = self.registers[int(register2)]

    def load(self, register, value):
        if value in self.data_references:
            self.registers[int(register)] = self.data_references[value]
        else:
            self.registers[int(register)] = int(value)

    def add(self, register1, register2):
        self.registers[int(register1)] = self.registers[int(register1)] + self.registers[int(register2)]

    def subtract(self, register1, register2):
        self.registers[int(register1)] = self.registers[int(register1)] - self.registers[int(register2)]
        if self.registers[int(register1)] < 0:
          self.flags[2] = 1
        elif self.registers[int(register1)] == 0:
          self.flags[1] = 1 

    def move(self, register1, register2):
        if int(register1) == 11:
            self.registers[int(register2)] = self.pointer + 2
        self.registers[int(register2)] = self.registers[int(register1)]

    def pop(self, register):
        self.registers[int(register)] = self.stack.pop()

    def push(self, register):
        self.stack.append(self.registers[int(register)])

    def jump(self, address):
        if address + ":" in self.labels:
            self.pointer = self.labels[address + ":"] - 2
        else:
            self.pointer = int(address)

    def jump_if_zero(self, register, address):
        if self.registers[int(register)] == 0:
            self.jump(address)

    def jump_if_one(self, register, address):
        if self.registers[int(register)] == 1:
            self.jump(address)


    def print_reg(self, register):
        print(self.registers[int(register)])

    def get_flag(self, register, register2):
        self.registers[int(register2)] = self.flags[int(register)]
        
    def halt(self):
        self.running = False

    def cmp(self, register1, register2):
        if self.registers[int(register1)] > self.registers[int(register2)]:
           self.flags[6] = 1
           self.flags[7] = 0
        elif self.registers[int(register1)] < self.registers[int(register2)]:
           self.flags[6] = 0
           self.flags[7] = 0
        else:
           self.flags[6] = 0
           self.flags[7] = 1

    def Ram(self):
        if self.bus[3] == 1:
            if self.bus[2] == 1:
                self.bus[1] = self.ram[self.bus[0]]
            else:
                self.ram[self.bus[0]] = self.bus[1]

    def run(self, instructions):
        self.running = True
        while self.running:
            instruction = instructions[self.pointer]
            print(f'Executing instruction: {instruction}')  # добавление для дебага
            self.instructions[instruction[0]](*instruction[1:])
            self.Ram()
            #сюда внешние устройства на шине
            print(f'Registers after execution: {self.registers}')  # добавление для дебага
            print(f'FLAGS after execution: {self.flags}')
            print(f'OUT BUS after execution: {self.bus}')
            self.pointer += 1
            self.tc += 1
            if self.pointer == len(instructions):
               self.pointer = 0

    def load_instructions(self, file_name):
        instructions = []
        with open(file_name, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.split('#')[0].strip()
                if line:
                    parts = line.split()
                    if parts[0] == 'LABEL':
                        self.labels[parts[1]] = len(instructions) + 1
                    elif 'DATA' in parts[0]:
                        name, value = line.split(": ")
                        self.data_references[name.strip()] = int(value.strip())
                    else:
                        instructions.append(parts)
        print(self.labels)
        print(self.data_references)
        return instructions


for root, dirs, files in os.walk("."):  
   for filename in files:
       if '.asm' in filename: print(filename)

BIOSN = input()

#вынос этого кода позволил сократить на 0,01-0,04 секунды
processor = Processor()
instructions = processor.load_instructions(BIOSN)

start_time = datetime.now()
processor.run(instructions)
end_time = datetime.now()

print( end_time - start_time, ' s | time to comp 1 comm', (end_time - start_time)/processor.tc )
