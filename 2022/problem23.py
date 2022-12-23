def find_halt():
    elves = set()
    lines = open("input23.txt").read().splitlines()
    part1 = -1
    for j in range(len(lines)):
        for i in range(len(lines[j])):
            if lines[j][i] == "#":
                elves.add( (i,j) )
    # d is proposals in-order, where the first coord of the tuple is the move-to position, but all 3 are checked
    d = [((0,-1),(-1,-1),(1,-1)), ((0,1),(-1,1),(1,1)), ((-1,0),(-1,-1),(-1,1)), ((1,0),(1,-1),(1,1))]
    adj = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    r = 0
    while True:
        prop = dict() #key is proposal, value is previous position; includes elves that don't move
        collisions = set() #saves collisions in case there are more than 2 colliding on a spot
        
        for x,y in elves:
            # check if there is any adjacent elf
            if sum( ((x+i,y+j) in elves) for i,j in adj ) == 0:
                prop[ (x,y) ] = (x,y)
            else:
                #propose movement
                proposal_added = False
                for p in range(len(d)):
                    check = d[(r+p)%len(d)]
                    if sum( ((x+i,y+j) in elves) for i,j in check ) == 0:
                        proposal_added = True
                        proposal = x+check[0][0],y+check[0][1]
                        if proposal not in prop and proposal not in collisions:
                            prop[ proposal ] = (x,y)
                        else:
                            prop[ (x,y) ] = (x,y)
                            if proposal in prop:
                                collision_src = prop[proposal]
                                prop[ collision_src ] = collision_src
                                del prop[proposal]
                            collisions.add( proposal )
                        break #proposed a spot, stop proposing
                if not proposal_added:
                    prop[ (x,y) ] = (x,y)
        
        elves = set(prop.keys())
        if (r+1) == 10:
            #find min/max coordinates for smallest rectangle
            min_x,max_x = min(elves,key=lambda item:item[0])[0], max(elves,key=lambda item:item[0])[0]
            min_y,max_y = min(elves,key=lambda item:item[1])[1], max(elves,key=lambda item:item[1])[1]
            part1 = ((max_x-min_x+1)*(max_y-min_y+1)) - len(elves)
        
        if sum(key != value for key,value in prop.items()) == 0:
            return part1, r+1 #stopped moving
        r += 1

part1,part2 = find_halt()
print("Part 1:",part1,"\nPart 2:",part2)