import sys
from collections import deque,defaultdict

min_x = min_y = sys.maxsize
max_x = max_y = -sys.maxsize
coords_claimed = dict()
claimed_count = defaultdict(int)
stack = deque()
for line in open("Resources/input6.txt"):
    x,y = [int(d) for d in line.split(", ")]
    min_x, max_x = min(min_x,x), max(max_x,x)
    min_y, max_y = min(min_y,y), max(max_y,y)
    stack.append( ((x,y),(x,y),0) ) #( next_coord, source, steps_from_source )
adjacency = [(-1,0),(1,0),(0,-1),(0,1)]
infinite_sources = set()
while stack:
    next_coord, source_coord, my_steps = stack.popleft()
    if next_coord in coords_claimed:
        claimer,steps = coords_claimed[next_coord]
        if claimer and claimer != source_coord and my_steps == steps:
            claimed_count[claimer] -= 1
            coords_claimed[next_coord] = (None, steps)
    else:
        coords_claimed[next_coord] = ( source_coord, my_steps )
        claimed_count[source_coord] += 1
        x,y = next_coord
        if x < min_x or x > max_x or y < min_y or y > max_y:
            infinite_sources.add(source_coord)
        else:
            for a,b in adjacency:
                stack.append( ((x+a,y+b), source_coord, my_steps+1) )

max_claimed = -1
for source_coord in claimed_count:
    if source_coord not in infinite_sources:
        max_claimed = max(max_claimed, claimed_count[source_coord])  
print("Part 1:",max_claimed)

region = 0
l = list(claimed_count.keys())
for x in range(min_x,max_x+1):
    for y in range(min_y,max_y+1):
        distance = 0
        for a,b in l:
            distance += abs(a-x)+abs(b-y)
        if distance < 10000:
            region += 1
print("Part 2:",region)