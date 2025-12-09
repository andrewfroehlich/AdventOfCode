def search(grid,max_adjacent,part2=False):
    adjacency = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    found,found_coords = 0,set()
    while True:
        for x,y in grid:
            adjacent_count = sum(1 for dx,dy in adjacency if (x+dx,y+dy) in grid)
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
    grid = set()
    for y,line in enumerate(open("input.txt")):
        for x,char in enumerate(line.strip()):
            if char == "@":
                grid.add((x,y))
    print("Part 1:",search(grid.copy(),4))
    print("Part 2:",search(grid.copy(),4,True))