#Part 1
f = open("input3.txt")
onesByPosition = [0 for i in range(12)]
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
print("Part 1:",gamma*epsilon)

#Part 2
f = open("input3.txt")
oxygen = []
co2 = []
#first loop to populate the lists
for line in f:
    if onesByPosition[0] == int(line[0]):
        oxygen.append(line.strip())
    else:
        co2.append(line.strip())
#now loop remaining indices
for index in range(1, len(onesByPosition)):
    if len(oxygen) > 1:
        ox1s = []
        ox0s = []
        for line in oxygen:
            if line[index] == '1':
                ox1s.append(line)
            else:
                ox0s.append(line)
        oxygen = ox1s if (len(ox1s) >= len(ox0s)) else ox0s
    if len(co2) > 1:
        co1s = []
        co0s = []
        for line in co2:
            if line[index] == '1':
                co1s.append(line)
            else:
                co0s.append(line)
        co2 = co0s if (len(co0s) <= len(co1s)) else co1s

print("Part 2:",int("".join(str(x) for x in oxygen), 2) * int("".join(str(x) for x in co2), 2))