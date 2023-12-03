def solve():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    
    sum1 = sum2 = 0
    symbols = set() # set of coordinates of all symbols for adjacency check
    gear_map = {} # map of gear coordinate to list of adjacent numbers
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] != "." and not lines[y][x].isdigit():
                symbols.add((x,y))
                if lines[y][x] == "*":
                    gear_map[(x,y)] = []
    adjacency = { (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1) }
    
    for y in range(len(lines)):
        current = ""
        valid = False
        adjacent_gears = set()
        for x in range(len(lines[y])):
            if lines[y][x].isdigit():
                # if digit, add onto current number and find adjacent symbols if not already found
                current += lines[y][x]
                if not valid:
                    for i,j in adjacency:
                        if (x+i,y+j) in symbols:
                            valid = True
                            if (x+i,y+j) in gear_map:
                                adjacent_gears.add((x+i,y+j))
                            break
            if not lines[y][x].isdigit() or x == len(lines[y])-1:
                # if not digit or end of the line, add the number if valid and reset tracking vars
                if current != "" and valid:
                    sum1 += int(current)
                    for i,j in adjacent_gears:
                        gear_map[(i,j)].append(int(current))
                    adjacent_gears = set()
                current = ""
                valid = False
    # for all gears, check if exactly 2 adjacent numbers and add the product to part 2
    for k,v in gear_map.items():
        if len(v) == 2:
            sum2 += v[0]*v[1]
    return sum1,sum2

if __name__ == "__main__":
    p1,p2 = solve()
    print("Part 1:",p1,"\nPart 2:",p2)