from collections import defaultdict

with open('day8.txt', 'r') as f:
    input = f.readlines()
    registers = defaultdict(int)
    for line in input:
        reg, instruction, number, condition, condReg, op, condNum = line.split()
        if eval("registers[condReg] " + op + condNum):
            if instruction == "inc":
                registers[reg] += int(number)
            else:
                registers[reg] -= int(number)

    print(max(registers.values()))
