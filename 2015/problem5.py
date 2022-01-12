def part1():
    part1 = 0
    for line in open("Resources/input5.txt"):
        vowels = line[0:1] in ('a','e','i','o','u')
        doubleLetter = False
        naughty = False
        for index in range(1,len(line)):
            if line[index] in ('a','e','i','o','u'):
                vowels += 1
            if line[index-1:index+1] in ("ab", "cd", "pq", "xy"):
                naughty = True
                break
            if line[index-1] == line[index]:
                doubleLetter = True
        if vowels >= 3 and doubleLetter and not naughty:
            part1 += 1
    return part1

def part2():
    part2 = 0
    for line in open("Resources/input5.txt"):
        pairs = dict()
        doubleLetter = False
        repeatSandwich = False
        pairs[line[0:2]] = 0
        for index in range(2,len(line)):
            double = line[index-1:index+1]
            if double in pairs:
                if pairs[double] != index-2:
                    doubleLetter = True
            else:
                pairs[double] = index-1
            
            if line[index-2] == line[index]:
                repeatSandwich = True
        if doubleLetter and repeatSandwich:
            part2 += 1
    return part2

print("Part 1:",part1())
print("Part 2:",part2())