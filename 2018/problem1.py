part1,part2,total = -1,-1,0
freq_list = [int(d) for d in open("Resources/input1.txt").readlines()]
s = set()
s.add(total)
while part2 == -1:
    for freq in freq_list:
        total += freq
        if part2 == -1 and total in s:
            part2 = total
        s.add(total)
    if part1 == -1:
        part1 = total
print("Part 1:",part1,"\nPart 2:",part2)