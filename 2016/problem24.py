import itertools
from collections import deque
import sys

def BFS(grid,src,dst):
    stack = deque()
    visited = set()
    stack.append( (src,0) )
    adjacency = [(1,0),(0,1),(-1,0),(0,-1)]
    while stack:
        coord,steps = stack.popleft()
        if coord == dst:
            return steps
        if coord in visited:
            continue
        visited.add(coord)
        x,y = coord
        for a,b in adjacency:
            if (x+a,y+b) in grid and (x+a,y+b) not in visited:
                stack.append( ((x+a,y+b),steps+1) )

lines = open("Resources/input24.txt").readlines()
ducts = set()
locations = dict()
for r in range(len(lines)):
    for c in range(len(lines[r].strip())):
        if lines[r][c] != "#":
            ducts.add( (r,c) )
            if lines[r][c].isnumeric():
                locations[int(lines[r][c])] = (r,c)

min_steps_graph = dict()
for src,dst in itertools.combinations(locations.keys(),2):
    min_steps = BFS(ducts,locations[src],locations[dst])
    min_steps_graph[(src,dst)] = min_steps
    min_steps_graph[(dst,src)] = min_steps

points_to_visit = list(locations.keys())
points_to_visit.remove(0) #starting with 0
min_part1 = min_part2 = sys.maxsize
for l in itertools.permutations(points_to_visit):
    last_point = 0
    current_path = 0
    for p in l:
        current_path += min_steps_graph[(last_point,p)]
        last_point = p
    min_part1 = min(current_path,min_part1)
    current_path += min_steps_graph[(last_point,0)]
    min_part2 = min(current_path,min_part2)
print("Part 1:",min_part1,"\nPart 2:",min_part2)