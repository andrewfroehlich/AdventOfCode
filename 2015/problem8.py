part1 = part2 = 0
for line in open("Resources/input8.txt"):
    s = line.strip()
    part1 += len(s) - (len(bytes(s, "utf-8").decode("unicode_escape")) - 2)
    part2 += s.count("\"") + s.count("\\") + 2
print("Part 1:",part1,"\nPart 2:",part2)