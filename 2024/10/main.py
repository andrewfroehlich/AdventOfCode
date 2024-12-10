from collections import deque

def dfs(grid, i, j):
    visited,nines,part2 = set(),set(),0
    dfs = deque()
    dfs.append( (i,j) )
    while dfs:
        x,y = dfs.popleft()
        visited.add( (x,y) )
        current = int(grid[x][y])
        if current == 9:
            part2 += 1
            nines.add( (x,y) )
            continue
        for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0<=(x+i)<len(grid) and 0<=(y+j)<len(grid[x+i]) and (x+i,y+j) not in visited and int(grid[x+i][y+j]) == current+1:
                dfs.append( (x+i,y+j) )
    return len(nines),part2 # part1 val, part2 val

def run():
    lines = open("input.txt").read().splitlines()
    part1,part2 = 0,0
    for x, line in enumerate(lines):
        for y, c in enumerate(line):
            if c == "0":
                delta1,delta2 = dfs(lines,x,y)
                part1 += delta1
                part2 += delta2
    return part1,part2

if __name__ == "__main__":
    part1,part2 = run()
    print("Part 1:",part1)
    print("Part 1:",part2)