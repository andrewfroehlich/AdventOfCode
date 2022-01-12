def run(part2):
    with open("Resources/input18.txt") as f:
        lines = f.read().splitlines()
    len_x = len(lines)
    len_y = len(lines[0])
    on_points = set()
    for l in range(len_x):
        for c in range(len_y):
            if lines[l][c] == '#':
                on_points.add( (l,c) )
    corners = [(0,0), (0,len_y-1), (len_x-1,0), (len_x-1,len_y-1)]
    if part2:
        for x,y in corners:
            on_points.add( (x,y) )
    adjacency = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for _ in range(100):
        new_on = set()
        for l in range(len_x):
            for c in range(len_y):
                adj_on = 0
                for x,y in adjacency:
                    adj_on += 1 if (l+x,c+y) in on_points else 0
                if (l,c) in on_points and adj_on in [2,3]:
                    new_on.add( (l,c) )
                elif (l,c) not in on_points and adj_on == 3:
                    new_on.add( (l,c) )
        on_points = new_on
        if part2:
            for x,y in corners:
                on_points.add( (x,y) )
    return len(on_points)

print("Part 1:",run(False))
print("Part 2:",run(True))