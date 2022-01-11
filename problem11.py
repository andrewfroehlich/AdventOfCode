f = open("input11.txt")
grid = []
adjacency = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
for line in f:
    gridLine = []
    for c in line.strip():
        gridLine.append(int(c))
    grid.append(gridLine)
flashes = 0
step = 0
toFlash = set()
flashed = set()
while True:
    #increment all
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            grid[x][y] += 1
            if grid[x][y] > 9:
                toFlash.add((x,y))
    #perform flashes in the step, set items that flashed to -1
    while len(toFlash) > 0:
        x,y = toFlash.pop()
        if grid[x][y] > 9:
            flashed.add((x,y))
            grid[x][y] = -1
            flashes += 1
            for i,j in adjacency:
                if x+i >= 0 and x+i < len(grid) and y+j >= 0 and y+j < len(grid[x+i]) and grid[x+i][y+j] > -1:
                    grid[x+i][y+j] += 1
                    if grid[x+i][y+j] > 9:
                        toFlash.add((x+i,y+j))
    #check if all flashed for part 2
    if len(flashed) == len(grid) * len(grid[0]):
        print("Part 2:",step+1) #step hasn't yet been incremented, so add 1
        break
    #set flashed items back to 0
    while len(flashed) > 0:
        x,y = flashed.pop()
        grid[x][y] = 0
    #increment step
    step += 1
    if step == 100:
        print("Part 1:",flashes)