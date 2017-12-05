from collections import Counter

with open('day4.txt', 'r') as f:
    input = [line.strip().split() for line in f.readlines()]
    valid = 0
    for line in input:
        if len(line) == len(set("".join(sorted(word)) for word in line)):
            valid += 1
    print(valid)