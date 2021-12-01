
def part1():
    f = open("C:\\Users\\fandrew\\Desktop\\AOC2021\\input1.txt")
    current = f.readline().strip()
    currentInt = 0
    last = 100000
    answer = 0
    while(current is not None and current != ''):
        currentInt = int(current)
        if currentInt > last:
            answer = answer+1
        last = currentInt
        current = f.readline().strip()
    return str(answer)

print("1: "+part1())

def part2():
    f = open("C:\\Users\\fandrew\\Desktop\\AOC2021\\input1.txt")
    current = f.readline().strip()
    currentInt = 0
    lastWindow = 100000
    currentWindow = 0
    answer = 0
    
    windows = [int(current)]
    current = f.readline().strip()
    while(current is not None and current != ''):
        currentInt = int(current)
        if len(windows) > 2:
            currentWindow = windows.pop(0)
            if currentWindow > lastWindow:
                answer = answer+1
            lastWindow = currentWindow
        for i in range(len(windows)):
            windows[i] = windows[i] + currentInt
        windows.append(currentInt)
        current = f.readline().strip()
    # Need one more run as the last loop "completes" a windows
    if windows.pop(0) > lastWindow:
        answer = answer+1
    return str(answer)

print("2: "+part2())