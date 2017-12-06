with open('day5.txt', 'r') as f:
    input = [int(line) for line in f.readlines()]
    steps = spot = 0
    while spot < len(input) and spot > -1:
        steps +=1
        jumpSteps = input[spot]
        input[spot] += 1
        spot += jumpSteps
    print(steps)
