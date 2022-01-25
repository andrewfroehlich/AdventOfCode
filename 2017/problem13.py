layers = dict()
max_layer = 0
for line in open("Resources/input13.txt"):
    lay,size = line.strip().split(": ")
    layers[int(lay)] = int(size)
    max_layer = max(max_layer,int(lay))

part1 = 0
for t in range(max_layer+1):
    if t in layers:
        if t % ((layers[t]-1)*2) == 0:
            part1 += t*layers[t]
print("Part 1:",part1)

delay = 0
while True:
    valid = True
    for t in range(max_layer+1):
        if t in layers:
            if (t+delay) % ((layers[t]-1)*2) == 0:
                valid = False
                break
    if valid:
        break
    delay += 1
print("Part 2:",delay)