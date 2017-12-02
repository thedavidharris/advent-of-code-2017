with open('day2.txt', 'r') as f:
    input = [[int(x) for x in line.split()] for line in f]
    print(sum([max(line) - min(line) for line in input]))