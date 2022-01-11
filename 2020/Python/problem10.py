def part1(jolts):
    current = threes = ones = 0
    for j in jolts:
        if j-current == 1:
            ones += 1
        elif j-current == 3:
            threes += 1
        current = j
    return ones*(threes+1)

def part2(jolts):
    indexToCount = dict()
    indexToCount[len(jolts)-1] = 1
    index = len(jolts) - 2
    for index in range(len(jolts)-2, -1, -1):
        currentCount = 0
        for j in range(index+1, index+4):
            if j < len(jolts) and jolts[index] + 3 >= jolts[j]:
                currentCount += indexToCount[j]
        indexToCount[index] = currentCount
    return indexToCount[0]
        
jolts = [int(j) for j in open("../Resources/problem10.txt").readlines()]
jolts.append(0)
jolts.sort()     
print("Part 1:",part1(jolts))
print("Part 2:",part2(jolts))