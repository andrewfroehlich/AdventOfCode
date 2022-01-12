def run(inp, part2):
    visited = set()
    x = y = r_x = r_y = 0
    visited.add ( (x,y) )
    for i in range(len(inp)):
        c = inp[i]
        if part2 and i % 2 == 0:
            if c == "^": r_y += 1
            elif c == "v": r_y -= 1
            elif c == "<": r_x -= 1
            elif c == ">": r_x += 1
            visited.add( (r_x,r_y) )
        else:
            if c == "^": y += 1
            elif c == "v": y -= 1
            elif c == "<": x -= 1
            elif c == ">": x += 1
            visited.add( (x,y) )
    return len(visited)

inp = open("Resources/input3.txt").readline().strip()
print("Part 1:",run(inp, False))
print("Part 2:",run(inp, True))