def run(part2):
    with open("../Resources/problem17.txt") as f:
        lines = f.read().splitlines()
    active = set()
    for l in range(len(lines)):
        for c in range(len(lines[l])):
            if lines[l][c] == "#":
                active.add((l,c,0,0))
    min_x = min_y = min_z = max_z = min_w = max_w = 0
    max_x = len(lines)
    max_y = len(lines[0])
    adjacency = set()
    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                if part2:
                    for w in range(-1,2):
                        adjacency.add( (x,y,z,w) )
                else:
                    adjacency.add( (x,y,z,0) )
    adjacency.discard( (0,0,0,0) )

    for step in range(1,7):
        new_active = set()
        for x in range(min_x-1, max_x+2):
            for y in range(min_y-1, max_y+2):
                for z in range(min_z-1, max_z+2):
                    for w in range(min_w-1, max_w+2):
                        adjacent_active = 0
                        for a,b,c,d in adjacency:
                            if (x+a,y+b,z+c,w+d) in active:
                                adjacent_active += 1
                        if ((x,y,z,w) in active and adjacent_active in (2,3)) or ((x,y,z,w) not in active and adjacent_active == 3):
                            new_active.add( (x,y,z,w) )
                            min_x = min(min_x,x)
                            min_y = min(min_y,y)
                            min_z = min(min_z,z)
                            min_w = min(min_w,w)
                            max_x = max(max_x,x)
                            max_y = max(max_y,y)
                            max_z = max(max_z,z)
                            max_w = max(max_w,w)
        active = new_active
    return len(active)

print("Part 1:",run(False))
print("Part 2:",run(True))