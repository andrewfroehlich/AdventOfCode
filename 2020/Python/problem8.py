lines = open("../Resources/problem8.txt").readlines()

def runInstruction(index,acc,swapIndex):
    inst,strValue = lines[index].strip().split()
    value = int(strValue)
    if inst == "jmp":
        if swapIndex == index:
            index += 1
        else:
            index += value
    else:
        if swapIndex == index:
            index += value
        else:
            index += 1
            if inst == "acc":
                acc += value
    return index,acc

def part1():
    acc = index = 0
    visited = set()
    while True:
        if index in visited:
            return acc
        visited.add(index)
        index,acc = runInstruction(index,acc,-1)

def part2():
    #find all indices of the loop
    loopIndices = set()
    acc = index = 0
    visited = set()
    while index not in loopIndices:
        if index in visited:
            loopIndices.add(index)
        visited.add(index)
        index,acc = runInstruction(index,acc,-1)
    #iterate over the loop indices swapping nop/jmp until hitting the end
    for swapIndex in loopIndices:
        if lines[swapIndex].strip().split()[0] == "acc":
            continue
        acc = index = 0
        visited = set()
        while index not in visited:
            visited.add(index)
            index,acc = runInstruction(index,acc,swapIndex)
            if index == len(lines):
                return acc

print("Part 1:",part1())
print("Part 2:",part2())