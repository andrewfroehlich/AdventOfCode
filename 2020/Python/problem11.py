def run(part1):
    with open("../Resources/problem11.txt") as f:
        lines = f.read().splitlines()
    unoccupied = set()
    occupied = set()
    floor = set()
    for l in range(len(lines)):
        for c in range(len(lines[l])):
            if lines[l][c] == 'L':
                unoccupied.add( (l,c) )
            elif lines[l][c] == '#':
                occupied.add( (l,c) )
            else:
                floor.add( (l,c) )
    adjacency = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    while True:
        new_occupied = set()
        new_unoccupied = set()
        changes = 0
        for l,c in unoccupied:
            occupied_adjacent = False
            for x,y in adjacency:
                c_x = l+x
                c_y = c+y
                while not part1 and (c_x,c_y) in floor:
                    c_x += x
                    c_y += y
                if (c_x,c_y) in occupied:
                    occupied_adjacent = True
                    break
            if not occupied_adjacent:
                changes += 1
                new_occupied.add( (l,c) )
            else:
                new_unoccupied.add( (l,c) )
        for l,c in occupied:
            occupied_adjacent = 0
            for x,y in adjacency:
                c_x = l+x
                c_y = c+y
                while not part1 and (c_x,c_y) in floor:
                    c_x += x
                    c_y += y
                if (c_x,c_y) in occupied:
                    occupied_adjacent += 1
            if (part1 and occupied_adjacent >= 4) or (not part1 and occupied_adjacent >= 5):
                changes += 1
                new_unoccupied.add( (l,c) )
            else:
                new_occupied.add( (l,c) )
        occupied = new_occupied
        unoccupied = new_unoccupied
        if changes == 0:
            return len(occupied)

print("Part 1:",run(True))
print("Part 2:",run(False))