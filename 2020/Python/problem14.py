def part1():
    memory = dict()
    andMaskInverse = orMask = ""
    for line in open("../Resources/problem14.txt"):
        raw = line.split(" = ")
        if line[0:4] == "mask":
            andMaskInverse = orMask = ""
            for c in raw[1].strip():
                andMaskInverse = andMaskInverse + ("1" if c == "0" else "0")
                orMask = orMask + ("1" if c == "1" else "0")
        else:
            value = int(raw[1])
            masked_value = (value & ~int(andMaskInverse, 2)) | int(orMask, 2)
            address = int(raw[0][4:-1])
            memory[address] = masked_value
    part1 = 0
    for k in memory:
        part1 += memory[k]
    return part1

def part2():
    memory = dict()
    orMask = ""
    floatingTwos = []
    for line in open("../Resources/problem14.txt"):
        raw = line.split(" = ")
        if line[0:4] == "mask":
            orMask = ""
            floatingTwos = []
            currentTwo = 1
            raw_mask = raw[1].strip()
            for i in range(len(raw_mask)-1,-1,-1):
                if raw_mask[i] == "X":
                    floatingTwos.append(currentTwo)
                orMask = ("1" if raw_mask[i] == "1" else "0") + orMask
                currentTwo = currentTwo * 2
        else:
            value = int(raw[1])
            address = int(raw[0][4:-1]) | int(orMask, 2)
            end_addresses = [address]
            temp = []
            for two in floatingTwos:
                for a in end_addresses:
                    temp.append(a | two)
                    temp.append(a & ~two)
                end_addresses.clear()
                for a in temp:
                    end_addresses.append(a)
                temp.clear()
            for a in end_addresses:
                memory[a] = value
    part2 = 0
    for k in memory:
        part2 += memory[k]
    return part2

print("Part 1:",part1())
print("Part 2:",part2())