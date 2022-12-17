def new_piece(piece_num, max_y):
    y = max_y+4
    if piece_num % 5 == 1:
        return [(2,y),(3,y),(4,y),(5,y)]
    elif piece_num % 5 == 2:
        return [(3,y),(2,y+1),(3,y+1),(4,y+1),(3,y+2)]
    elif piece_num % 5 == 3:
        return [(2,y),(3,y),(4,y),(4,y+1),(4,y+2)]
    elif piece_num % 5 == 4:
        return [(2,y),(2,y+1),(2,y+2),(2,y+3)]
    else:
        return [(2,y),(3,y),(2,y+1),(3,y+1)]

def solve(air,piece_count,starting_piece,starting_airi,first_clear=False,find_loop=False):
    airi,max_y,floor,new_coords = starting_airi,0,0,[]
    occupied,loop_start = set(),(-1,-1)
    if find_loop:
        loop_start = (starting_piece,airi%len(air))

    for piece in range(starting_piece,piece_count+1):
        coords = new_piece(piece,max_y)
        at_rest = False
        
        while not at_rest:
            # try to puff air
            if air[airi%len(air)] == "<":
                new_coords = [(x-1,y) for (x,y) in coords]
            else:
                new_coords = [(x+1,y) for (x,y) in coords]
            airi += 1
            valid = True
            for x,y in new_coords:
                if (x,y) in occupied or x < 0 or x > 6:
                    valid = False
            if valid:
                coords = new_coords
            
            # try to move down
            new_coords = [(x,y-1) for (x,y) in coords]
            
            for x,y in new_coords:
                if (x,y) in occupied or y <= floor:
                    at_rest = True
            if not at_rest:
                coords = new_coords
        # occupy the coordinates
        occupied.update(coords)
        
        # if the full y-coordinate is now filled, clear out older points and move the floor up
        new_floor = -1
        for y in range(min(coords,key=lambda item:item[1])[1], max(coords,key=lambda item:item[1])[1]+1):
            if set([(x,y) for x in range(7)]).issubset(occupied):
                new_floor = y
        if new_floor > -1:
            floor = new_floor
            occupied = set([(x,y) for x,y in occupied if not y<=floor])
            if len(occupied) == 0:
                #full clear occurred
                if first_clear:
                    return (piece,floor,airi%len(air))
                #find loop logic
                if find_loop and (airi%len(air)) == loop_start[1]:
                    return (piece-loop_start[0]+1, floor, loop_start[1])  
        
        # check new max_y
        max_y = max(max_y, max(coords,key=lambda item:item[1])[1])
    return max_y

def part2(air, pieces):
    # find the first time the board is fully cleared tetris-style to start looking for loops
    first_clear_step,first_clear_floor,loop_airi = solve(air,pieces,1,0,True,False)
    # find the length of the loop back to an empty board with the same air puff index (airi)
    loop_steps,loop_floors,loop_airi = solve(air,pieces,first_clear_step+1,loop_airi,False,True)

    # the first step we need to run is the last step before we hit our final piece count
    starting_step = pieces - ((pieces-first_clear_step) % (loop_steps))
    # we can find what floor we should be at there by the first loop plus the loop floor amount times the loop count
    starting_floor = first_clear_floor + (((pieces-first_clear_step)//(loop_steps))*loop_floors)
    
    # run the simulation again from the starting step to see additional floors to add
    additional_floors = solve(air,pieces,(starting_step+1),loop_airi)
    return starting_floor + additional_floors
    
air = open("input17.txt").readline().strip()
print("Part 1:",solve(air,2022,1,0))
print("Part 2:",part2(air,1000000000000))