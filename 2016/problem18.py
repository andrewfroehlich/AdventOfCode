line = open("Resources/input18.txt").readline().strip()
traps = set()
for i in range(len(line)):
    if line[i] == "^":
        traps.add( (i,0) )

part1_traps = part2_traps = len(traps)
for y in range(1,400000):
    new_traps = set()
    for x in range(len(line)):
        b = str(int((x-1,y-1) in traps)) + str(int((x,y-1) in traps)) + str(int((x+1,y-1) in traps))
        if b in ("100","001","110","011"):
            new_traps.add( (x,y) )
    part1_traps += len(new_traps) if y < 40 else 0
    part2_traps += len(new_traps)
    traps = new_traps
    
print("Part 1:", (40*len(line))-part1_traps)
print("Part 2:", (400000*len(line))-part2_traps)