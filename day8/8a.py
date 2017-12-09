from collections import defaultdict

input = [line.strip("\n").replace("dec", "-=").replace("inc", "+=")  for line in open('day8.txt').readlines()]

registers = defaultdict(int)
for line in input:
    line += " else 0"
    exec(line, {}, registers)

print(max(registers.values()))
