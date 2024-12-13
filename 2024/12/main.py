from collections import deque

def search(grid,x,y):
    perim,area = 0,0
    init = (x,y)
    plant = grid[x][y]
    visited = set([(x,y)])
    dfs = deque([(x,y)])
    while dfs:
        x,y = dfs.popleft()
        area += 1
        for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0<=(x+i)<len(grid) and 0<=(y+j)<len(grid[x+i]) and (x+i,y+j) not in visited and grid[x+i][y+j] == plant:
                visited.add( (x+i,y+j) )
                dfs.append( (x+i,y+j) )
            elif (x+i,y+j) not in visited :
                perim += 1

    # use visited to count corners
    corners = 0
    for x, y in visited:
        corners += ( x - 1, y ) not in visited and ( x, y - 1 ) not in visited
        corners += ( x + 1, y ) not in visited and ( x, y - 1 ) not in visited
        corners += ( x - 1, y ) not in visited and ( x, y + 1 ) not in visited
        corners += ( x + 1, y ) not in visited and ( x, y + 1 ) not in visited
        corners += ( x - 1, y ) in visited and ( x, y - 1 ) in visited and ( x - 1, y - 1 ) not in visited
        corners += ( x + 1, y ) in visited and ( x, y - 1 ) in visited and ( x + 1, y - 1 ) not in visited
        corners += ( x - 1, y ) in visited and ( x, y + 1 ) in visited and ( x - 1, y + 1 ) not in visited
        corners += ( x + 1, y ) in visited and ( x, y + 1 ) in visited and ( x + 1, y + 1 ) not in visited
    return area*perim,area*corners,visited

def run():
    visited = set()
    part1,part2 = 0,0
    lines = open("input.txt").read().splitlines()
    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            if (x,y) not in visited:
                p1,p2,traversed = search(lines,x,y)
                visited.update(traversed)
                part1 += p1
                part2 += p2
    return part1,part2

if __name__ == "__main__":
    part1,part2 = run()
    print("Part 1:",part1)
    print("Part 2:",part2)