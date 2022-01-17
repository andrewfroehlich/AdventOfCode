on = set()
len_x = 50
len_y = 6
for line in open("Resources/input8.txt"):
    if line[0:4] == "rect":
        coords = line.split()[1].split("x")
        for x in range(int(coords[0])):
            for y in range(int(coords[1])):
                on.add( (x,y) )
    else:
        _,rc,raw_coord,_,val = line.split()
        coord = int(raw_coord[2:])
        new_on = set()
        if rc == "row":
            for c in range(len_x):
                if (c,coord) in on:
                    new_on.add( ((c+int(val))%len_x,coord) )
                    on.remove( (c,coord) )
        else: #"col"
            for r in range(len_y):
                if (coord,r) in on:
                    new_on.add( (coord, (r+int(val))%len_y) )
                    on.remove( (coord,r) )
        #print("New On",len(new_on))
        for new_x,new_y in new_on:
            on.add( (new_x,new_y) )
print("Part 1:",len(on))

grid = [[" " for _ in range(50)] for _ in range(6)]
for x,y in on:
    grid[y][x] = "#"
for row in grid:
    print("".join(row))

#  # ###   ##    ## #### #    ###   ##  #### ####
#  # #  # #  #    # #    #    #  # #  # #       #
#  # #  # #  #    # ###  #    ###  #    ###    #
#  # ###  #  #    # #    #    #  # #    #     #
#  # #    #  # #  # #    #    #  # #  # #    #
 ##  #     ##   ##  #    #### ###   ##  #### ####