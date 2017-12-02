import itertools

with open('day2.txt', 'r') as f:
    sum = 0
    for line in f:
        input = map(int, line.split())
        input = [list(row) for row in list(itertools.combinations(input, 2))]
        for row in input:
            if max(row) % min(row) == 0:
                sum += max(row)/min(row)
print(sum)