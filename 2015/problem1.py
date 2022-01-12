inp = open("Resources/input1.txt").readline().strip()
part1 = part2 = 0
for i in range(len(inp)):
    part1 += 1 if inp[i] == "(" else -1
    if part1 == -1 and part2 == 0:
        part2 = i+1
print("Part 1:",part1,"\nPart 2:",part2)