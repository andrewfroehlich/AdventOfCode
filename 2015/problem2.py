part1 = part2 = 0
for line in open("Resources/input2.txt"):
    d = [int(c) for c in line.split("x")]
    part1 += 2*d[0]*d[1] + 2*d[1]*d[2] + 2*d[2]*d[0] + min(d[0]*d[1],d[1]*d[2],d[2]*d[0])
    part2 += d[0]*d[1]*d[2] + 2*(d[0]+d[1]+d[2]) - 2*max(d[0],d[1],d[2])
print("Part 1:",part1,"\nPart 2:",part2)