lines = open("Resources/input3.txt").readlines()
direction = {"R":(1,0), "U":(0,1), "L":(-1,0), "D":(0,-1)}

#iterate over wire1, adding all points to a point dictionary
w1 = dict()
x=y=steps=0
for d in lines[0].split(","):
    i,j = direction[d[0:1]]
    for _ in range(int(d[1:])):
        x,y = x+i,y+j
        steps += 1
        if (x,y) not in w1:
            w1[(x,y)] = steps

#iterate over wire2 finding intersections, only keeping the minimum distance/steps one
part1=part2=x=y=steps=0
for d in lines[1].split(","):
    i,j = direction[d[0:1]]
    for _ in range(int(d[1:])):
        x,y = x+i,y+j
        steps += 1
        if (x,y) in w1:
            #part1 uses distance
            distance = abs(x) + abs(y)
            if 0 < distance and (part1 == 0 or distance < part1):
                part1 = distance
            #part2 uses total steps
            if part2 == 0 or (steps + w1[(x,y)]) < part2:
                part2 = steps + w1[(x,y)]

print("Part 1:",part1,"\nPart 2:",part2)