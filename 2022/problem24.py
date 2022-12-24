from collections import deque

def run(starting_step=0,flip_target=False):
    blizz0 = dict()
    lines = open("input24.txt").read().splitlines()
    blizz_marks = {"^":(0,-1), "v":(0,1), "<":(-1,0), ">":(1,0)}
    for j in range(1,len(lines)-1):
        for i in range(1,len(lines[j])-1):
            if lines[j][i] in blizz_marks:
                blizz0[(i-1,j-1)] = blizz_marks[ lines[j][i] ]
    
    start,target = (lines[0].index(".")-1,-1), (lines[-1].index(".")-1,len(lines)-2)
    if flip_target:
        temp = start
        start = target
        target = temp
    min_x,max_x,min_y,max_y = 0,len(lines[1])-3,0,len(lines)-3
    moves = [(1,0),(0,1),(0,0),(-1,0),(0,-1)] #down, right, wait, left, up
    bfs = deque( [(start[0],start[1],starting_step)] ) #x,y,steps
    visited = set( [(start[0],start[1],starting_step)] ) #x,y,steps
    
    current_blizz = set(blizz0.keys())
    last_step = 0 # says how many steps the current blizz represents
    while True:
        x,y,steps = bfs.popleft()
        steps += 1
        if steps > last_step:
            current_blizz = set()
            for s,move in blizz0.items():
                bx,by = s
                dx,dy = move
                current_blizz.add( ((bx + steps*dx)%(max_x+1), (by + steps*dy)%(max_y+1)) )
            last_step = steps
        
        for i,j in moves:
            nx,ny = x+i,y+j
            if (nx,ny) == target:
                return steps
            if ((nx,ny) == start or (min_x<=nx<=max_x and min_y<=ny<=max_y)) and (nx,ny,steps) not in visited and (nx,ny) not in current_blizz:
                visited.add( (nx,ny,steps) )
                bfs.append( (nx,ny,steps) )

part1 = run()
print("Part 1:", part1)
print("Part 2:", run(run(part1,True)))