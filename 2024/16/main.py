import heapq
from collections import defaultdict

def process_input():
    c_x,c_y = 0,0
    target = (0,0)
    walls = set()
    for y, line in enumerate(open("input.txt").read().splitlines()):
        for x, c in enumerate(line):
            if c == "S":
                c_x,c_y = x,y
            elif c == "E":
                target = (x,y)
            elif c == "#":
                walls.add( (x,y) )
    return walls,target,c_x,c_y

def part1(walls,target,c_x,c_y):
    dirs = [(1,0),(0,1),(-1,0),(0,-1)] # E, N, W, S
    c_dir = 0 # current direction index

    pq = []
    heapq.heappush(pq, (0, c_x, c_y, c_dir))
    visited = set()
    visited.add( (c_x,c_y,c_dir) )
    while pq:
        score,i,j,d = heapq.heappop(pq)
        if (i,j) == target:
            return score
        p_i,p_j = i + dirs[d][0],j + dirs[d][1]
        if (p_i,p_j,d) not in visited and (p_i,p_j) not in walls:
            visited.add( (p_i, p_j, d) )
            heapq.heappush(pq, (score+1, p_i, p_j, d))
        if (i,j, (d-1+4)%4) not in visited:
            visited.add( (i, j, (d-1+4)%4) )
            heapq.heappush(pq, (score+1000, i, j, (d-1+4)%4))
        if (i,j, (d+1)%4) not in visited:
            visited.add( (i, j, (d+1)%4) )
            heapq.heappush(pq, (score+1000, i, j, (d+1)%4))
    return -1

def part2(target_score,walls,target,c_x,c_y):
    dirs = [(1,0),(0,1),(-1,0),(0,-1)] # E, N, W, S
    c_dir = 0 # current direction index

    pq = []
    heapq.heappush(pq, (0, c_x, c_y, c_dir, [(c_x,c_y)]))
    visited = set()
    visited.add( (c_x,c_y,c_dir) )

    paths_per_point = defaultdict(set)
    paths_per_point[(c_x,c_y,c_dir)].add() #can I just add on this point and keep track of the previous point to save the paths?

    while pq:
        score,i,j,d = heapq.heappop(pq)
        if (i,j) == target:
            return score
        p_i,p_j = i + dirs[d][0],j + dirs[d][1]
        if (p_i,p_j,d) not in visited and (p_i,p_j) not in walls:
            visited.add( (p_i, p_j, d) )
            heapq.heappush(pq, (score+1, p_i, p_j, d))
        if (i,j, (d-1+4)%4) not in visited:
            visited.add( (i, j, (d-1+4)%4) )
            heapq.heappush(pq, (score+1000, i, j, (d-1+4)%4))
        if (i,j, (d+1)%4) not in visited:
            visited.add( (i, j, (d+1)%4) )
            heapq.heappush(pq, (score+1000, i, j, (d+1)%4))
    return -1

if __name__ == "__main__":
    walls,target,c_x,c_y = process_input()
    part1 = part1(walls,target,c_x,c_y)
    print("Part 1:",part1)
    print("Part 2:",part2(part1,walls,target,c_x,c_y))