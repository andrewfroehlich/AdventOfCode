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
        if len(windows) > 2:
            currWindow = windows.pop(0)
            if currWindow > prevWindow:
                answer += 1
            prevWindow = currWindow
        for i in range(len(windows)):
            windows[i] += int(line)
        windows.append(int(line))
    # Need one more run as the last loop "completes" a windows
    if windows.pop(0) > prevWindow:
        answer += 1
    return answer

print("Part 1:",part1())
print("Part 2:",part2())