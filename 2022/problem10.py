addx = part1 = 0
extra_cycle = False
cycle = X = 1
part2 = [["." for _ in range(40)] for _ in range(6)]

for line in open("input10.txt"):
    if line.strip() != "noop":
        addx = int(line.strip().split()[1])
        extra_cycle = True
    for _ in range(2 if extra_cycle else 1):
        if (cycle-20) % 40 == 0:
            part1 += cycle*X
        if X-1 <= ((cycle-1) % 40) <= X+1:
            part2[(cycle-1)//40][(cycle-1)%40] = "#"
        cycle += 1
    X += addx
    addx = 0
    extra_cycle = False

print("Part 1:",part1,"\nPart 2:")
for i in range(len(part2)):
    print("".join(part2[i]))