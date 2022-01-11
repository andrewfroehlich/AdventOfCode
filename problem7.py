import statistics
import math

def part1(crabs):
    median = statistics.median(crabs)
    fuel = 0
    for i in crabs:
        fuel += abs(i - median)
    return int(fuel)

def part2(crabs):
    mean = statistics.mean(crabs)
    meanFloor = int(math.floor(mean))
    meanCeil = int(math.ceil(mean))
    fuelFloor = fuelCeil = 0
    for i in crabs:
        nFloor = abs(i - meanFloor)
        fuelFloor += int((nFloor*(nFloor+1))/2)
        nCeil = abs(i - meanCeil)
        fuelCeil += int((nCeil*(nCeil+1))/2)
    return min(fuelFloor,fuelCeil)

crabList = open("input7.txt").readline()
crabs = [int(num) for num in crabList.split(',')]
print("Part 1:", part1(crabs))
print("Part 2:", part2(crabs))