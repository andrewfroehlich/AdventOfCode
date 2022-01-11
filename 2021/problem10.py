f = open("input10.txt")
closeToOpen = {')': '(', ']': '[', '}': '{', '>': '<'}
illegalScore = {')': 3, ']': 57, '}': 1197, '>': 25137}
completeScore = {'(': 1, '[': 2, '{': 3, '<': 4}

part1 = 0
part2 = []
for line in f:
    stack = []
    for c in line.strip():
        if c in closeToOpen:
            if closeToOpen[c] != stack.pop():
                part1 += illegalScore[c]
                break
        else:
            stack.append(c)
    else:
        score = 0
        while bool(stack):
            score = (score * 5) + completeScore[stack.pop()]
        part2.append(score)

print("Part 1:",part1)
part2.sort()
print("Part 2:",part2[int(len(part2)/2)])