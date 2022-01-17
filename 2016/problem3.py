valid = 0
lines = open("Resources/input3.txt").readlines()
for line in lines:
    sides = [int(s) for s in line.strip().split()]
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        valid += 1
print("Part 1:",valid)

valid = 0
for i in range(len(lines)//3):
    for j in range(3):
        sides = [int(lines[3*i].split()[j]), int(lines[3*i + 1].split()[j]), int(lines[3*i + 2].split()[j])]
        #print(sides)
        sides.sort()
        if sides[0] + sides[1] > sides[2]:
            valid += 1
print("Part 2:",valid)