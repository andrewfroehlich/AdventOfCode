import re

def cube_wrap(i,j,d):
    if d == 0 and i== 151: #1-R
        return 100, 151-j, 2
    elif d == 1 and j == 51: #1-D
        return 100, 50 + (i-100), 2
    elif d == 3 and j == 0 and i > 100: #1-U
        return i - 100, 200, 3
    elif d == 3 and j == 0 and 51 <= i <= 100: #2-U
        return 1, 150 + (i - 50), 0
    elif d == 2 and i == 50 and j < 51: #2-L
        return 1, 151 - j, 0
    elif d == 2 and i == 50 and 51 <= j <= 100: #3-L
        return j - 50, 101, 1
    elif d == 0 and i == 101 and 51 <= j <= 100: #3-R
        return 100 + (j - 50), 50, 3
    elif d == 0 and i == 101 and 101 <= j <= 150: #4-R
        return 150, 151 - j, 2
    elif d == 1 and j == 151: #4-D
        return 50, 150 + (i - 50), 2
    elif d == 2 and i == 0 and 101 <= j <= 150: #5-L
        return 51, 151 - j, 0
    elif d == 3 and j == 100: #5-U
        return 51, 50 + i, 0
    elif d == 2 and i == 0 and j >= 151: #6-L
        return 50 + (j - 150), 1, 1
    elif d == 0 and i == 51: #6-R
        return 50 + (j - 150), 150, 3
    elif d == 1 and j == 201: #6-D
        return i + 100, 1, 1
    else:
        print("Something broke!",i,j,d)

def solve(cube=False):
    lines = open("input22.txt").read().splitlines()
    m,walls = set(),set()
    max_x,max_y = 0,len(lines)-2
    for row in range(len(lines)-2):
        max_x = max(len(lines[row]),max_x)
        for col in range(len(lines[row])):
            if lines[row][col] == ".":
                m.add( (col+1,row+1) )
            elif lines[row][col] == "#":
                walls.add( (col+1,row+1) )

    direction = [(1,0),(0,1),(-1,0),(0,-1)] # facing: R,D,L,U
    # set starting point, facing R
    x, y, d = lines[0].index(".")+1, 1, 0

    path = re.split('(\d+)',lines[-1])
    for cur in path:
        if cur == "":
            continue
        elif cur.isnumeric():
            for steps in range(int(cur)):
                i,j = x+direction[d][0],y+direction[d][1]
                if (i,j) in m:
                    x,y = i,j
                elif (i,j) in walls:
                    break
                else: 
                    #wrap around
                    if not cube:
                        new_d = d #direction doesn't change
                        if d == 0: #R
                            i = 1
                        elif d == 1: #D
                            j = 1
                        elif d == 2: #L
                            i = max_x
                        else: #U
                            j = max_y
                        
                        #find the first point on this side
                        while (i,j) not in m and (i,j) not in walls:
                            i,j = i+direction[d][0],j+direction[d][1]
                    else:
                        i,j,new_d = cube_wrap(i,j,d)
                    
                    #if its a wall, break and don't change x,y,d. Otherwise, update all
                    if (i,j) in walls:
                        break
                    else:
                        x,y,d = i,j,new_d
        else:
            d = (d + 1)%len(direction) if cur == "R" else (d + len(direction) - 1)%len(direction)
    return (1000*y + 4*x + d)

print("Part 1:",solve())
print("Part 2:",solve(True))