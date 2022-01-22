line = open("Resources/input1.txt").readline().strip()
part1 = part2 = 0
for i in range(len(line)):
    if line[i] == line[(i+1)%len(line)]:
        part1 += int(line[i])
    if line[i] == line[(i+(len(line)//2))%len(line)]:
        part2 += int(line[i])
print("Part 1:",part1,"\nPart 2:",part2)