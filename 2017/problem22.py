def part1():
    direction = [(0,-1),(1,0),(0,1),(-1,0)] # -> turn right, <- turn left
    grid = set()
    lines = open("Resources/input22.txt").readlines()
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == "#":
                grid.add( (col,row) )
    c_y = len(lines)//2
    c_x = len(lines[c_y].strip())//2
    dir_i = 0

    part1 = 0
    for burst in range(10000):
        if (c_x,c_y) in grid:
            dir_i = (dir_i + 1) % 4
            grid.remove((c_x,c_y))
        else:
            dir_i = (4 + dir_i - 1) % 4
            grid.add((c_x,c_y))
            part1 += 1
        
        c_x,c_y = c_x + direction[dir_i][0], c_y + direction[dir_i][1]
    return part1

def part2():
    direction = [(0,-1),(1,0),(0,1),(-1,0)] # -> turn right, <- turn left
    grid = dict()
    lines = open("Resources/input22.txt").readlines()
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == "#":
                grid[(col,row)] = "I"
    c_y = len(lines)//2
    c_x = len(lines[c_y].strip())//2
    dir_i = 0

    part2 = 0
    for burst in range(10000000):
        if (c_x,c_y) in grid:
            if grid[(c_x,c_y)] == "W":
                grid[(c_x,c_y)] = "I"
                part2 += 1
            elif grid[(c_x,c_y)] == "I":
                dir_i = (dir_i + 1) % 4
                grid[(c_x,c_y)] = "F"
            elif grid[(c_x,c_y)] == "F":
                dir_i = (dir_i + 2) % 4
                del grid[(c_x,c_y)]
        else:
            dir_i = (4 + dir_i - 1) % 4
            grid[(c_x,c_y)] = "W"
        
        c_x,c_y = c_x + direction[dir_i][0], c_y + direction[dir_i][1]
    return part2

print("Part 1:",part1())
print("Part 2:",part2())