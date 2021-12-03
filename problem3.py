#Part 1
f = open("input3.txt")
onesByPosition = [0 for i in range(len(f.readline().strip()))]
for line in f:
    for index in range(len(line.strip())):
        onesByPosition[index] += (1 if line[index] == '1' else -1)
index = len(onesByPosition)-1
multiplier = 1
gamma = epsilon = 0
while index >= 0:
    onesByPosition[index] = 1 if onesByPosition[index] >= 0 else 0
    gamma += multiplier * onesByPosition[index]
    epsilon += multiplier  * (0 if onesByPosition[index] > 0 else 1)
    multiplier = multiplier * 2
    index -= 1
print("Part 1:", gamma * epsilon)

#Part 2
oxygen = []
co2 = []
#first loop to populate the lists from the file
for line in f:
    if onesByPosition[0] == int(line[0]):
        oxygen.append(line.strip())
    else:
        co2.append(line.strip())
#now loop remaining indices
for index in range(1, len(onesByPosition)):
    if len(oxygen) > 1:
        a1 = []
        a0 = []
        for line in oxygen:
            if line[index] == '1':
                a1.append(line)
            else:
                a0.append(line)
        oxygen = a1 if (len(a1) >= len(a0)) else a0
    if len(co2) > 1:
        a1 = []
        a0 = []
        for line in co2:
            if line[index] == '1':
                a1.append(line)
            else:
                a0.append(line)
        co2 = a0 if (len(a0) <= len(a1)) else a1

print("Part 2:", int(oxygen[0], 2) * int(co2[0], 2))