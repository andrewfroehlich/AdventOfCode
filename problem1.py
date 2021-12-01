
def part1():
    f = open("input1.txt")
    currInt = answer = 0
    prev = 100000
    current = f.readline().strip()
    while(current != ''):
        currInt = int(current)
        if currInt > prev:
            answer += 1
        prev = currInt
        current = f.readline()
    return str(answer)

print("1: "+part1())

def part2():
    f = open("input1.txt")
    currInt = currWindow = answer = 0
    prevWindow = 100000
    
    windows = [int(f.readline())]
    current = f.readline()
    while(current != ''):
        currInt = int(current)
        if len(windows) > 2:
            currWindow = windows.pop(0)
            if currWindow > prevWindow:
                answer += 1
            prevWindow = currWindow
        for i in range(len(windows)):
            windows[i] = windows[i] + currInt
        windows.append(currInt)
        current = f.readline()
    # Need one more run as the last loop "completes" a windows
    if windows.pop(0) > prevWindow:
        answer += 1
    return str(answer)

print("2: "+part2())