from collections import Counter

counters = [Counter() for _ in range(len(open("Resources/input6.txt").readline().strip()))]
for line in open("Resources/input6.txt"):
    for i in range(len(line.strip())):
        counters[i].update(line[i])
part1 = part2 = ""
for c in counters:
    part1 += c.most_common(1)[0][0]
    part2 += c.most_common()[-1][0]
print("Part 1:",part1,"\nPart 2:",part2)