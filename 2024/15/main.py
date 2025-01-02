def part1():
    grid_lines,movement_lines = open("input.txt").read().split("\n\n")
    robot_x,robot_y = 0,0
    walls,boxes = set(),set()
    #only needed for printing:
    max_x,max_y = -1,-1
    for y, line in enumerate(grid_lines.split("\n")):
        max_y = max(max_y,y)
        for x, c in enumerate(line):
            max_x = max(max_x,x)
            if c == "@":
                robot_x,robot_y = x,y
            elif c == "O":
                boxes.add( (x,y) )
            elif c == "#":
                walls.add( (x,y) )

    dir = {"<":(-1,0), "^":(0,-1), ">":(1,0), "v":(0,1)}
    for move in ''.join(movement_lines.split("\n")):
        del_x,del_y = dir[move]
        proposed_coords = (robot_x+del_x, robot_y+del_y)
        if proposed_coords in walls:
            continue # can't move into a wall, end movement
        if proposed_coords not in boxes:
            robot_x,robot_y = proposed_coords
        else:
            # not a wall but there is a box, iterate in the same direction until we hit a space or a wall
            box_proposed_coords = (proposed_coords[0]+del_x, proposed_coords[1]+del_y)
            while box_proposed_coords not in walls and box_proposed_coords in boxes:
                box_proposed_coords = (box_proposed_coords[0]+del_x, box_proposed_coords[1]+del_y)
            if box_proposed_coords not in walls:
                boxes.add(box_proposed_coords)
                boxes.remove(proposed_coords)
                robot_x,robot_y = proposed_coords

    #for debug, print the box
    for y in range(max_y+1):
        line = ""
        for x in range(max_x+1):
            if x == robot_x and y == robot_y:
                line += "@"
            elif (x,y) in boxes:
                line += "O"
            elif (x,y) in walls:
                line += "#"
            else:
                line += "."
        print(line)

    #GPS values
    return sum([100*y + x for (x,y) in boxes])

def part2():
    grid_lines,movement_lines = open("input.txt").read().split("\n\n")
    robot_x,robot_y = 0,0
    walls,boxes = set(),set() #boxes is now just the left bracket, the right is assumed
    #only needed for printing:
    max_x,max_y = -1,-1
    for y, line in enumerate(grid_lines.split("\n")):
        max_y = max(max_y,y)
        for x, c in enumerate(line):
            max_x = max(max_x,2*x)
            if c == "@":
                robot_x,robot_y = 2*x,y
            elif c == "O":
                boxes.add( (2*x,y) )
            elif c == "#":
                walls.add( (2*x,y) )
                walls.add( (2*x + 1,y) )
    #for debug, print the box
    for y in range(max_y+1):
        line = ""
        for x in range(max_x+1):
            if x == robot_x and y == robot_y:
                line += "@"
            elif (x,y) in boxes:
                line += "["
            elif (x,y) in walls:
                line += "#"
            elif (x-1,y) in boxes:
                line += "]"
            else:
                line += "."
        print(line)

    dir = {"<":(-1,0), "^":(0,-1), ">":(1,0), "v":(0,1)}

    for move in ''.join(movement_lines.split("\n")):
        del_x,del_y = dir[move]
        proposed_coords = (robot_x+del_x, robot_y+del_y)
        if proposed_coords in walls:
            continue # can't move into a wall, end movement
        if proposed_coords not in boxes and (robot_x+del_x-1,robot_y+del_y) not in boxes:
            robot_x,robot_y = proposed_coords
        else:
            # not a wall but there is a box, iterate in the same direction until we hit a space or a wall
            boxes_to_move,boxes_to_place = set(),set()

            #box_to_move = proposed_coords if proposed_coords in boxes else (robot_x+del_x-1,robot_y+del_y)
            #boxes_to_move.add(box_to_move)
            #boxes_to_place.add( (box_to_move[0]+del_x,box_to_move[1]+del_y) )

            curr_x,curr_y = proposed_coords
            while (curr_x,curr_y) not in walls and ((curr_x,curr_y) in boxes or (curr_x-1,curr_y) in boxes):
                if (curr_x,curr_y) not in boxes_to_move and (curr_x-1,curr_y) not in boxes_to_move: #haven't already marked this box
                    box_to_move = (curr_x,curr_y) if (curr_x,curr_y) in boxes else (curr_x-1,curr_y)
                    if box_to_move not in boxes:
                        print("Error!")
                    boxes_to_move.add(box_to_move)
                    new_box_placement = (box_to_move[0]+del_x,box_to_move[1]+del_y)
                    if new_box_placement in walls or (new_box_placement[0]+1,new_box_placement[1]) in walls:
                        break
                    boxes_to_place.add(new_box_placement)
                curr_x,curr_y = curr_x+del_x,curr_y+del_y #increment last if we don't run the move statement once before the loop

            if (curr_x,curr_y) not in walls and len(boxes_to_move) == len(boxes_to_place): # if they're different sizes, we hit a wall mid-way
                for (x,y) in boxes_to_move:
                    boxes.remove( (x,y) )
                for box_to_place in boxes_to_place:
                    boxes.add(box_to_place)
                robot_x,robot_y = proposed_coords

    #for debug, print the box
    for y in range(max_y+1):
        line = ""
        for x in range(max_x+1):
            if x == robot_x and y == robot_y:
                line += "@"
            elif (x,y) in boxes:
                line += "["
            elif (x,y) in walls:
                line += "#"
            elif (x-1,y) in boxes:
                line += "]"
            else:
                line += "."
        print(line)
    #GPS values
    return sum([100*y + x for (x,y) in boxes])

if __name__ == "__main__":
    #before,update_lines = process_input()
    print("Part 1:",part1())
    print("Part 2:",part2())