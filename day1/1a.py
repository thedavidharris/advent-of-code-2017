with open('day1.txt', 'r') as f:
    input = f.read()

print sum(int(x[0]) for x in zip(input, input[1:] + input[0]) if x[0] == x[1])