from collections import deque,defaultdict

def biggest_island(grid,adjacency):
    visited = set()
    stack = deque()
    island_size = defaultdict(int)
    for x,y in grid:
        stack.append( (x,y,(x,y)) ) #x, y, origin point 
        
    while stack:
        x,y,origin = stack.popleft()
        if (x,y) in visited:
            continue
        visited.add( (x,y) )
        island_size[origin] += 1
        for a,b in adjacency:
            if (x+a,y+b) not in visited and (x+a,y+b) in grid:
                stack.appendleft( (x+a,y+b,origin) )
    
    v = list(island_size.values())
    k = list(island_size.keys())
    return k[v.index(max(v))], max(v)

grid = set()
points = []
for line in open("Resources/input10.txt"):
    pos_x,pos_y = [int(p) for p in line[10:24].split(",")]
    vel_x,vel_y = [int(v) for v in line[36:42].split(",")]
    grid.add( (pos_x,pos_y) )
    points.append( (pos_x,pos_y,vel_x,vel_y) )

adjacency = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
step = max_island = 0
max_island_origin = None
printing = False
while True: 
    new_grid = set()
    for i in range(len(points)):
        x,y,vel_x,vel_y = points[i]
        new_grid.add( (x+vel_x,y+vel_y) )
        points[i] = ( x+vel_x,y+vel_y,vel_x,vel_y )
    grid = new_grid
    step += 1
    
    #if step>10000:  #uncomment to speed it up, knowing that the input is over 10k steps away
    max_island_origin,max_island = biggest_island(grid,adjacency)
    if max_island > 12: #large island implies letters are forming
        print("Step",step)
        printing = True
        i,j = max_island_origin
        for y in range(j-20,j+25): #print around a point in the island
            row = []
            for x in range(i-60,i+75):
                row.append( "#" if (x,y) in grid else "." )
            print("".join(row))
        print("-----")
    elif max_island < 9 and printing:
        break #we had a large island, but we no longer due, stop the program