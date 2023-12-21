from collections import deque

def parse_file():
    lines = open("input.txt").read().splitlines()
    m,s = set(),None
    for y in range(-1,len(lines)+1):
        for x in range(-1,len(lines[0])+1):
            if y in (-1,len(lines)) or x in (-1,len(lines[0])) or lines[y][x] == "#":
                m.add( (x,y) )
            elif lines[y][x] == "S":
                s = (x,y)
    return m,s,lines
    
def run_steps(m,s,steps):
    bfs = deque( [(s[0],s[1],0) ] )
    visited = set([s])
    evens_and_odds = [1,0]
    adjacency = [(1,0),(-1,0),(0,1),(0,-1)]
    while bfs:
        x,y,step = bfs.popleft()
        if step < steps:
            for i,j in adjacency:
                if (x+i,y+j) not in m and (x+i,y+j) not in visited:
                    visited.add( (x+i,y+j) )
                    evens_and_odds[(step+1)%2] += 1
                    bfs.append( (x+i,y+j,step+1) )
    return evens_and_odds

if __name__ == "__main__":
    m,s,lines = parse_file()
    print("Part 1:", run_steps(m,s,64)[0])
    
    # math required summarized here: https://github.com/villuna/aoc23/wiki/A-Geometric-solution-to-advent-of-code-2023,-day-21
    even_full,odd_full = run_steps(m,s,200) # any number of steps enough to saturate
    even_inner_corner,odd_inner_corner = run_steps(m,s,len(lines)//2) # the steps for the inner diamond, the distance from S to the edge
    even_corners,odd_corners = even_full-even_inner_corner,odd_full-odd_inner_corner # outer corners is full minus inner diamond
    n = (26501365 - (len(lines)//2)) // len(lines) # n is the number of grids out we will go
    p2 = ((n+1)**2 * odd_full) + (n**2 * even_full) - ((n+1) * odd_corners) + (n * even_corners) # this math explained in the link above
    print("Part 2:", p2)