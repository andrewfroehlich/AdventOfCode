import sys
from collections import deque

def part1(grid,max_x,max_y):
    part1 = 0
    for xa in range(max_x+1):
        for ya in range(max_y+1):
            if grid[(xa,ya)][0] > 0: #non-empty
                for xb in range(max_x+1):
                    for yb in range(max_y+1):
                        if (xa,ya) == (xb,yb):
                            continue
                        if grid[(xa,ya)][0] <= grid[(xb,yb)][1]:
                            part1 += 1
    return part1

def find_shortest_path(from_x,from_y,to_x,to_y,grid,empty_size,avoid_coord):
    stack = deque()
    traversed = set()
    if avoid_coord:
        traversed.add(avoid_coord)
    adjacency = [("R",1,0),("U",0,-1),("D",0,1),("L",-1,0)]
    stack.append( (from_x,from_y,"") )
    while stack:
        x,y,path = stack.popleft()
        if (x,y) in traversed:
            continue
        traversed.add((x,y))
        if (x,y) == (to_x,to_y):
            return path
        else: 
            for d,i,j in adjacency:
                if (x+i,y+j) in grid and grid[(x+i,y+j)][0] <= empty_size:
                    stack.append( (x+i,y+j,path+d) )

grid = dict()
max_x = max_y = 0
empty_x = empty_y = -1
for line in open("Resources/input22.txt"):
    if line[0:4] != "/dev":
        continue
    raw_node,_,used,avail,_ = line.split()
    _,raw_x,raw_y = raw_node.split("-")
    max_x = max(max_x,int(raw_x[1:]))
    max_y = max(max_y,int(raw_y[1:]))
    grid[(int(raw_x[1:]),int(raw_y[1:]))] = (int(used[:-1]),int(avail[:-1]))
    if int(used[:-1]) == 0:
        empty_x,empty_y = int(raw_x[1:]),int(raw_y[1:])
print("Part 1:",part1(grid,max_x,max_y))

#find the optimal path from the top corner to final target to follow
empty_size = grid[empty_x,empty_y][1]
total_steps = 0
corner_to_target = find_shortest_path(max_x,0,0,0,grid,empty_size,None)

#continually move the empty around the payload into the optimal path to move the payload to the final target
payload_loc = (max_x,0)
for step in corner_to_target:
    #move the empty into the target path
    empty_target_x,empty_target_y = payload_loc
    if step == "L":
        empty_target_x -= 1
    elif step == "D":
        empty_target_y += 1
    elif step == "R":
        empty_target_x += 1
    else: #"U"
        empty_target_y -= 1
    empty_path = find_shortest_path(empty_x,empty_y,empty_target_x,empty_target_y,grid,empty_size,payload_loc)
    total_steps += len(empty_path)
    
    #swap empty and payload and reset pointers
    empty_x,empty_y = payload_loc
    payload_loc = (empty_target_x,empty_target_y)
    total_steps += 1
print("Part 2:",total_steps)