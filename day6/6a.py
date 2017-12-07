from copy import copy

with open('day6.txt', 'r') as f:
    currentState = [int(line) for line in f.read().split()]

    turns = 0
    previousStates = []

    while currentState not in previousStates:
        previousStates.append(copy(currentState))
        big = max(currentState)
        index = currentState.index(big)
        currentState[index] = 0
        while big > 0:
            index = (index+1)%len(currentState)
            currentState[index] += 1
            big -= 1
        turns += 1
        
    print(turns)