def part1():
    f = open("input2.txt")
    depth = horiz = 0
    current = f.readline()
    while(current != ''):
        command = current.split(' ')
        if command[0] == "forward":
            horiz += int(command[1])
        else:
            depth += (1 if command[0] == "down" else -1) * int(command[1])
        current = f.readline()
    return horiz*depth

def part2():
    f = open("input2.txt")
    depth = horiz = aim = 0
    current = f.readline()
    while(current != ''):
        command = current.split(' ')
        if command[0] == "forward":
            horiz += int(command[1])
            depth += aim * int(command[1])
        else:
            aim += (1 if command[0] == "down" else -1) * int(command[1])
        current = f.readline()
    return horiz*depth

print("Part 1:",part1())
print("Part 2:",part2())