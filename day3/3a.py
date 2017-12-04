import math

with open('day3.txt', 'r') as f:
    input = int(f.read())

closestSquareRoot = math.ceil(math.sqrt(input))

sideLength = closestSquareRoot + 1 if closestSquareRoot % 2 == 0 else closestSquareRoot
print(sideLength)

stepsToReachSide = (sideLength-1)/2
print(stepsToReachSide)

cycleLength = input - ((sideLength - 2)**2)
innerOffset = cycleLength % (sideLength - 1)

distance = stepsToReachSide + abs(innerOffset - stepsToReachSide)
print(distance)