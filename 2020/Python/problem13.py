def part1():
    with open("../Resources/problem13.txt") as f:
        lines = f.read().splitlines()
    timestamp = int(lines[0])
    buses = []
    for c in lines[1].split(","):
        if c != "x":
            buses.append(int(c))
    target = timestamp
    while True:
        for b in buses:
            if target % b == 0:
                return b * (target - timestamp)
        target += 1

def part2():
    with open("../Resources/problem13.txt") as f:
        lines = f.read().splitlines()
    busToOffset = dict()
    rawBusInput = lines[1].split(",")
    largestBus = 0
    for offset in range(len(rawBusInput)):
        if rawBusInput[offset] != "x":
            busValue = int(rawBusInput[offset])
            busToOffset[busValue] = offset
            if busValue > largestBus:
                largestBus = busValue
    
    currentTarget = largestBus - busToOffset[largestBus]
    del busToOffset[largestBus]
    incrementer = largestBus
    while True:
        for bus in list(busToOffset):
            if (currentTarget + busToOffset[bus]) % bus == 0:
                incrementer = incrementer * bus
                del busToOffset[bus]
                if len(busToOffset) == 0:
                    return currentTarget
        currentTarget += incrementer

print("Part 1:",part1())
print("Part 2:",part2())