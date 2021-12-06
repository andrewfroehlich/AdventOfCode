def solve(simDays):
    inputList = open("input6.txt").readline().split(",")
    fishCount = len(inputList)
    fish = [0 for i in range(9)]
    for i in inputList:
        fish[int(i)] += 1
    day = 0
    while day < simDays:
        zeroFish = fish.pop(0)
        fish.append(zeroFish) #0 becomes 8
        fish[6] += zeroFish #0 also becomes 6
        fishCount += zeroFish #keep count of added fish
        day += 1
    return fishCount

print("Part 1:", solve(80))
print("Part 2:", solve(256))