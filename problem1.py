def part1():
    f = open("input1.txt")
    answer = 0
    prev = 100000
    for line in f:
        if int(line) > prev:
            answer += 1
        prev = int(line)
    return answer

def part2():
    f = open("input1.txt")
    currWindow = answer = 0
    prevWindow = 100000
    windows = []
    for line in f:
        for i in range(len(windows)):
            windows[i] += int(line)
        windows.append(int(line))
        if len(windows) > 2:
            currWindow = windows.pop(0)
            if currWindow > prevWindow:
                answer += 1
            prevWindow = currWindow
    return answer

print("Part 1:",part1())
print("Part 2:",part2())