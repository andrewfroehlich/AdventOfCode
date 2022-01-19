ranges = set()
for line in open("Resources/input20.txt"):
    low,high = line.strip().split("-")
    ranges.add( (int(low),int(high)) )

value = 0
allowed_IPs = 0
part1 = -1
while value <= 4294967295:
    to_remove = []
    max_blocked = -1
    for l,h in ranges:
        if h < value:
            to_remove.append( (l,h) )
        if l <= value and value < h:
            max_blocked = max(max_blocked,h)
            to_remove.append( (l,h) )
    if max_blocked == -1:
        if part1 == -1:
            part1 = value
        allowed_IPs += 1
        value += 1
    else:
        value = max_blocked+1
        for l,h in to_remove:
            ranges.remove( (l,h) )

print("Part 1:",part1,"\nPart 2:",allowed_IPs)