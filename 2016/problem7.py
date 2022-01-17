import re

def hasABBA(line):
    for i in range(len(line)-3):
        if line[i] == line[i+3] and line[i+1] == line[i+2] and line[i] != line[i+1]:
            return True
    return False

def findABA(line):
    aba = []
    for i in range(len(line)-2):
        if line[i] == line[i+2] and line[i] != line[i+1]:
            aba.append(line[i:i+3])
    return aba

part1 = part2 = 0
for line in open("Resources/input7.txt"):
    spl = re.split(r'\[|\]', line.strip())
    foundPart1Out = foundPart1In = False
    abaOutside = []
    abaInside = []
    for i in range(len(spl)):
        if i % 2 == 0:
            abaOutside.extend(findABA(spl[i]))
            if not foundPart1Out and i % 2 == 0 and hasABBA(spl[i]):
                foundPart1Out = True
        else:
            abaInside.extend(findABA(spl[i]))
            if hasABBA(spl[i]):
                foundPart1In = True
    
    if foundPart1Out and not foundPart1In:
        part1 += 1
    
    foundPart2 = False
    for bab in abaInside:
        aba = bab[1]+bab[0]+bab[1]
        if aba in abaOutside:
            foundPart2 = True
            break
    if foundPart2:
        part2 += 1
print("Part 1:",part1,"\nPart 2:",part2)