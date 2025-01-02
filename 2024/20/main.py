from collections import deque

def process_input():
    c_x,c_y,max_x,max_y,target = 0,0,0,0,(0,0)
    walls = set()
    for y, line in enumerate(open("input.txt").read().splitlines()):
        for x, c in enumerate(line):
            if c == "S":
                c_x,c_y = x,y
            elif c == "E":
                target = (x,y)
            elif c == "#":
                walls.add( (x,y) )
    return walls,target,c_x,c_y,max(walls, key=lambda p: p[0])[0],max(walls, key=lambda p: p[1])[1]

def bfs(walls,target,c_x,c_y,max_x,max_y,cheats=False,no_cheat_best=-1):
    bfs = deque()
    visited = set()
    cheat_block = (0,0) if not cheats else (-1,-1)
    bfs.append( (c_x,c_y,0,cheat_block,(-1,-1)) ) #current x, current y, steps, cheat block coordinate if used, move after cheat block
    visited.add( (c_x,c_y,cheat_block,(-1,-1)) )
    results = 0
    while bfs:
        x,y,steps,cb,cb2 = bfs.popleft()
        for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx,ny = x+i,y+j
            if (nx,ny) == target:
                if not cheats:
                    return steps
                else:#elif no_cheat_best - steps >= 5:
                    results += 1
            elif not cheats or cb != (-1,-1): # not at target, can't cheat
                if 0<nx<max_x and 0<ny<max_y and (nx,ny) not in walls:
                    cb2 = (nx,ny) if cheats and cb2 == (-1,-1) else cb2
                    if (nx,ny,cb,cb2) not in visited:
                        bfs.append( (nx,ny,steps+1,cb,cb2) )
                        visited.add( (nx,ny,cb,cb2) )
            else: # not at target, cheats are on and unused
                if 0<nx<max_x and 0<ny<max_y:
                    if (nx,ny) in walls:
                        cb = (nx,ny)
                    if (nx,ny,cb,cb2) not in visited:
                        bfs.append( (nx,ny,steps+1,cb,cb2) )
                        visited.add( (nx,ny,cb,cb2) )
    return results


if __name__ == "__main__":
    walls,target,c_x,c_y,max_x,max_y = process_input()
    no_cheat_best = bfs(walls,target,c_x,c_y,max_x,max_y)
    print(no_cheat_best)
    part1 = bfs(walls,target,c_x,c_y,max_x,max_y,True,no_cheat_best)
    print(part1)