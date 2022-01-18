def find_first_valid_time(discs):
    time = 0
    while True:
        valid = True
        for d in discs:
            if (time + d[0] + d[2]) % d[1] != 0:
                valid = False
                break
        if valid:
            return time
        time += 1

discs = []
for line in open("Resources/input15.txt"):
    _,disc,_,slots,_,_,_,_,_,_,_,pos = line.strip().split()
    discs.append( (int(disc[1:]),int(slots),int(pos[:-1])) )
print("Part 1:",find_first_valid_time(discs))
discs.append( (len(discs)+1, 11, 0) )
print("Part 2:",find_first_valid_time(discs))