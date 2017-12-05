print(sum(len(line) == len(set(line)) for line in [line.strip().split() for line in open('day4.txt').readlines()]))
