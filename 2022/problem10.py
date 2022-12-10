addx = extra_cycles = part1 = 0
cycle = X = 1
part2 = [["." for _ in range(40)] for _ in range(6)]

for line in open("input10.txt"):
    if line.strip() != "noop":
        addx = int(line.strip().split()[1])
        extra_cycles = 1
    for i in range(extra_cycles+1):
        if (cycle-20) % 40 == 0 and cycle < 221:
            part1 += cycle*X
        if X-1 <= ((cycle-1) % 40) <= X+1:
            part2[(cycle-1)//40][(cycle-1)%40] = "#"
        cycle += 1
    extra_cycles = 0
    if addx != 0:
        X += addx
        addx = 0

print("Part 1:",part1,"\nPart 2:")
for i in range(len(part2)):
    print("".join(part2[i]))