import re
import math
import time

def safety_factor(grid,len_x,len_y):
    quads = [0,0,0,0]
    for x,y,_,_ in grid:
        if x < len_x//2:
            if y < len_y//2:
                quads[0] += 1
            elif y > len_y//2:
                quads[1] += 1
        elif x > len_x//2:
            if y < len_y//2:
                quads[2] += 1
            elif y > len_y//2:
                quads[3] += 1
    return math.prod(quads)

def print_tree(pts,len_x,len_y):
    for j in range(len_y):
        print(''.join(['#' if (i,j) in pts else '.' for i in range(len_x)]))

def run(steps,len_x,len_y,is_part2):
    grid,pts = [],set()
    for line in open("input.txt"):
        x,y,vx,vy = [int(d) for d in re.findall(r'-?\d+', line)]
        grid.append( (x,y,vx,vy) )
        pts.add( (x,y) )

    for step in range(steps):
        new_grid,new_pts = [],set()
        for x,y,vx,vy in grid:
            x = (x + vx + len_x) % len_x
            y = (y + vy + len_y) % len_y
            new_grid.append( (x,y,vx,vy) )
            new_pts.add( (x,y) )
        grid = new_grid
        pts = new_pts
        if is_part2:
            # check if there are many points in a row on a y-axis
            has_line = False
            for x,y in pts:
                if all((x+i, y) in pts for i in range(8)):
                    has_line = True
                    break
            if has_line:
                print("STEP",step+1)
                print_tree(pts,len_x,len_y)
                time.sleep(2)
    return safety_factor(grid,len_x,len_y)

if __name__ == "__main__":
    print("Part 1:",run(100,101,103,False))
    print("Part 2:",run(10000,101,103,True))