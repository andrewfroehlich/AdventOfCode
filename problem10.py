f = open("input10.txt")
closeToOpen = {')': '(', ']': '[', '}': '{', '>': '<'}
illegalScore = {')': 3, ']': 57, '}': 1197, '>': 25137}
completeScore = {'(': 1, '[': 2, '{': 3, '<': 4}

part1 = 0
part2 = []
for line in f:
    stack = []
    corrupted = False
    for c in line.strip():
        if c in closeToOpen:
            match = stack.pop()
            if closeToOpen[c] != match:
                part1 += illegalScore[c]
                corrupted = True
                break
        else:
            stack.append(c)
    if not corrupted:
        score = 0
        while len(stack) > 0:
            score = (score * 5) + completeScore[stack.pop()]
        part2.append(score)

print("Part 1:",part1)
part2.sort()
print("Part 2:",part2[int(len(part2)/2)])