on = set() #part 1
brightness = dict() #part 2
for line in open("Resources/input6.txt"):
    spl_line = line.split()
    if spl_line[0] == "turn":
        spl_line.pop(0)
    coord1 = (int(spl_line[1].split(",")[0]), int(spl_line[1].split(",")[1]))
    coord2 = (int(spl_line[3].split(",")[0]), int(spl_line[3].split(",")[1]))
    for x in range(coord1[0],coord2[0]+1):
        for y in range(coord1[1],coord2[1]+1):
            if (x,y) not in brightness:
                brightness[(x,y)] = 0
            
            if spl_line[0] == "on":
                on.add( (x,y) )
                brightness[(x,y)] += 1
            elif spl_line[0] == "off":
                on.discard( (x,y) )
                brightness[(x,y)] = brightness[(x,y)] - 1 if brightness[(x,y)] > 0 else 0
            else: #toggle 
                if (x,y) in on:
                    on.remove( (x,y) )
                else:
                    on.add( (x,y) )
                brightness[(x,y)] += 2
print("Part 1:", len(on), "\nPart 2:", sum(brightness.values()))