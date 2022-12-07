current = 0
lines = []
for line in open("input1.txt"):
    if line == "\n":
        lines.append(current)
        current = 0
    else:
        current += int(line)
lines.sort(reverse=True)
print("Part 1: "+str(lines[0]))
print("Part 2: "+str(lines[0]+lines[1]+lines[2]))