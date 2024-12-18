from collections import deque

def run(nanoseconds,max_x,max_y):
    walls = set()
    last_wall_added = (-1,-1)
    lines = open("input.txt").read().splitlines()
    for i in range(nanoseconds):
        x,y = [int(d) for d in lines[i].split(",")]
        walls.add( (x,y) )
        last_wall_added = (x,y)

    bfs,visited = deque(),set()
    bfs.append( (0,0,0) ) #x,y,steps
    visited.add( (0,0) )
    while bfs:
        x,y,steps = bfs.popleft()
        if (x,y) == (max_x,max_y):
            return steps,-1
        for i,j in [(1,0),(0,1),(0,-1),(-1,0)]:
            a,b = x+i,y+j
            if (a,b) not in visited and (a,b) not in walls and 0<=a<=max_x and 0<=b<=max_y:
                bfs.append( (a,b,steps+1) )
                visited.add( (a,b) )
    return last_wall_added # no path found, return last wall added

def part2(nanoseconds,max_x,max_y):
    while True:
        x,y = run(nanoseconds,max_x,max_y)
        if y > -1:
            return x,y
        nanoseconds += 1

if __name__ == "__main__":
    print("Part 1:",run(1024,70,70)[0])
    print("Part 2:",",".join(str(d) for d in part2(1025,70,70)))