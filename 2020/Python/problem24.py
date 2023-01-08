paths = open("../Resources/problem24.txt").read().splitlines()
direct = {"w":(-2,0), "e":(2,0), "sw":(-1,-1), "se":(1,-1), "nw":(-1,1), "ne":(1,1)}
black_sides = set()
for path in paths:
    x,y,i = 0,0,0
    while i < len(path):
        if path[i] in direct:
            x,y = x+direct[path[i]][0],y+direct[path[i]][1]
            i += 1
        else:
            x,y = x+direct[path[i:i+2]][0],y+direct[path[i:i+2]][1]
            i += 2
    if (x,y) in black_sides:
        black_sides.remove( (x,y) )
    else:
        black_sides.add( (x,y) )
print("Part 1:",len(black_sides))

adj = direct.values()
for day in range(100):
    new_black_sides = set()
    for x in range( min(black_sides, key = lambda t: t[0])[0]-2, max(black_sides, key = lambda t: t[0])[0]+3 ):
        for y in range( min(black_sides, key = lambda t: t[1])[1]-1, max(black_sides, key = lambda t: t[1])[1]+2 ):
            if (x%2 == 0 and y%2 != 0) or (x%2 != 0 and y%2 == 0):
                continue
            
            if (x,y) in black_sides:
                adjacent = 0
                for a,b in adj:
                    if (x+a,y+b) in black_sides:
                        adjacent += 1
                        if adjacent > 2:
                            break
                if adjacent in (1,2):
                    new_black_sides.add( (x,y) )
            else:
                adjacent = 0
                for a,b in adj:
                    if (x+a,y+b) in black_sides:
                        adjacent += 1
                        if adjacent > 2:
                            break
                if adjacent == 2:
                    new_black_sides.add( (x,y) )
    black_sides = new_black_sides.copy()
print("Part 2:",len(black_sides))