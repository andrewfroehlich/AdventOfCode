lines = open("Resources/input13.txt").readlines()
directions = [ (-1,0), (0,-1), (1,0), (0,1) ] #0-left, 1-up, 2-right, 3-down
turns = [-1, 0, 1] # index updates to directions, left straight right
grid = dict()
occupied = set()
carts = [] #y, x, direction_index, turn_index
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if not lines[i][j].strip():
            continue
        if lines[i][j] in ('/','\\','-','|','+'):
            grid[(j,i)] = lines[i][j]
        elif lines[i][j] in ('>','<'):
            grid[(j,i)] = '-'
            carts.append( (i,j,(2 if lines[i][j] == '>' else 0),0) )
            occupied.add( (j,i) )
        elif lines[i][j] in ('^','v'):
            grid[(j,i)] = '|'
            carts.append( (i,j,(1 if lines[i][j] == '^' else 3),0) )
            occupied.add( (j,i) )

part1 = ""
while len(carts) > 1:
    carts.sort()
    new_carts = []
    index = 0
    while index < len(carts):
        y,x,dir_i,turn_i = carts[index]
        index += 1
        occupied.remove( (x,y) )
        x,y = x + directions[dir_i][0], y + directions[dir_i][1]
        if (x,y) in occupied:
            occupied.remove( (x,y) )
            if not part1:
                part1 = "{},{}".format(x,y)
            #find the crashed car in the remaining carts or ones already processed
            i = 0
            while i < len(new_carts):
                if new_carts[i][1] == x and new_carts[i][0] == y:
                    del new_carts[i]
                else:
                    i += 1
            i = index
            while i < len(carts):
                if carts[i][1] == x and carts[i][0] == y:
                    del carts[i]
                else:
                    i += 1
        else:
            occupied.add( (x,y) )
            if grid[(x,y)] == '+':
                dir_i = (4 + dir_i + turns[turn_i]) % 4
                turn_i = (turn_i + 1) % 3
            elif grid[(x,y)] == '/':
                dir_i = 3 - dir_i
            elif grid[(x,y)] == '\\':
                dir_i = dir_i + 1 if dir_i % 2 == 0 else dir_i - 1
            new_carts.append( (y,x,dir_i,turn_i) )
    carts = new_carts

print("Part 1:",part1,"\nPart 2: {},{}".format(carts[0][1],carts[0][0]))