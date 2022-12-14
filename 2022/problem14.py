walls,sand = set(),set()
max_y = 0

for line in open("input14.txt").read().splitlines():
    raw_points = line.split(" -> ")
    cur_x,cur_y = [int(d) for d in raw_points[0].split(",")]
    for i in range(1,len(raw_points)):
        x,y = [int(d) for d in raw_points[i].split(",")]
        for a in range(min(x,cur_x),max(x,cur_x)+1):
            for b in range(min(y,cur_y),max(y,cur_y)+1):
                walls.add( (a,b) )
        max_y = max(max_y, cur_y, y)
        cur_x,cur_y = x,y

part1 = -1
sand_paths = [ (0,1),(-1,1),(1,1) ]
while (500,0) not in sand: 
    x,y = 500,0
    while True:
        while (x,y+1) not in walls and (x,y+1) not in sand and (y+1 < max_y+2):
            y += 1
            if y > max_y and part1 == -1:
                part1 = len(sand)
        if (x-1,y+1) not in walls and (x-1,y+1) not in sand and (y+1 < max_y+2):
            x,y = x-1,y+1
        elif (x+1,y+1) not in walls and (x+1,y+1) not in sand and (y+1 < max_y+2):
            x,y = x+1,y+1
        else:
            break
    sand.add( (x,y) )
print("Part 1:",part1,"\nPart 2:",len(sand))