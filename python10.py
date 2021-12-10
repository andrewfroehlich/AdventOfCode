def part1():
    f = open("input10b.txt")
    closeToOpen = {')': '(', ']': '[', '}': '{', '>': '<'}
    illegalScore = {')': 3, ']': 57, '}': 1197, '>': 25137}
    
    answer = 0
    stack = []
    for line in f:
        for c in line:
            if c in closeToOpen:
                match = stack.pop()
                if closeToOpen[c] != match:
                    answer += illegalScore[match]
                    break
            else:
                stack.append(c)
    return answer

def part2():
    return -1

print("Part 1:",part1())
print("Part 2:",part2())