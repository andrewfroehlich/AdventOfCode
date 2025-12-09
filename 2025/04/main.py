def search(grid,max_x,max_y,max_adjacent,part2=False):
    adjacency = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    found,found_coords = 0,set()
    while True:
        for x,y in grid:
            adjacent_count = 0
            for dx,dy in adjacency:
                if (x+dx,y+dy) in grid:
                    adjacent_count += 1
            if adjacent_count < max_adjacent:
                found_coords.add((x,y))
        if not part2:
            return len(found_coords)
        if len(found_coords) == 0:
            return found
        found += len(found_coords)
        grid -= found_coords
        found_coords = set()

if __name__ == "__main__":
    grid,max_x,max_y = set(),-1,-1
    for y,line in enumerate(open("input.txt")):
        max_y = y
        for x,char in enumerate(line.strip()):
            max_x = max(max_x,x)
            if char == "@":
                grid.add((x,y))
    print("Part 1:",search(grid,max_x,max_y,4))
    print("Part 2:",search(grid,max_x,max_y,4,True))