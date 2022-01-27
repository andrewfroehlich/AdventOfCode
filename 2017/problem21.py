rotate3 = ["012345678","630741852","876543210","258147036","210543876","036147258","678345012","852741630"]
rotate2 = ["0123","2031","3210","1302","1032","0213","2301","3120"]

key3,key2 = dict(),dict()
for line in open("Resources/input21.txt"):
    twoLine = (line.index("=>") < 9)
    src,dst = line.replace("/","").strip().split(" => ")
    for r in (rotate2 if twoLine else rotate3):
        src_rotate = ["." for _ in range(len(r))]
        for i in range(len(r)):
            src_rotate[int(r[i])] = src[i]
        
        if twoLine:
            key2["".join(src_rotate)] = dst
        else:
            key3["".join(src_rotate)] = dst

grid = set()
grid.update([(1,0),(2,1),(0,2),(1,2),(2,2)])
size = 3
box_2 = [(0,0),(1,0),(0,1),(1,1)]
box_3 = [(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)]
box_4 = [(0,0),(1,0),(2,0),(3,0),(0,1),(1,1),(2,1),(3,1),(0,2),(1,2),(2,2),(3,2),(0,3),(1,3),(2,3),(3,3)]

part1 = -1
for iteration in range(18):
    new_grid = set()
    if size % 2 == 0:
        new_size = (size//2) * 3
        for x in range(size//2):
            for y in range(size//2):
                current_box = []
                for a,b in box_2:
                    current_box.append( "#" if (2*x + a, 2*y + b) in grid else "." )
                new_box = key2["".join(current_box)]
                for i in range(len(new_box)):
                    if new_box[i] == "#":
                        new_grid.add( (3*x + box_3[i][0] , 3*y + box_3[i][1]) ) 
    else:
        new_size = (size//3) * 4
        for x in range(size//3):
            for y in range(size//3):
                current_box = []
                for a,b in box_3:
                    current_box.append( "#" if (3*x + a, 3*y + b) in grid else "." )
                new_box = key3["".join(current_box)]
                for i in range(len(new_box)):
                    if new_box[i] == "#":
                        new_grid.add( (4*x + box_4[i][0] , 4*y + box_4[i][1]) )
    
    grid = new_grid
    size = new_size
    if iteration == 4:
        part1 = len(grid)
print("Part 1:",part1,"\nPart 2:",len(grid))