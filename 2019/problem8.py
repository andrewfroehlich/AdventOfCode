image = open("Resources/input8.txt").readline()
layers = []
w,l = 25,6
for i in range(0,len(image),w*l):
    layers.append( image[i:i+w*l] )

min_0,part1 = len(layers[0]),-1
for layer in layers:
    zeroes,ones,twos = 0,0,0
    for digit in layer:
        if digit == "0":
            zeroes += 1
        elif digit == "1":
            ones += 1
        elif digit == "2":
            twos += 1
    if zeroes < min_0:
        part1 = ones * twos
        min_0 = zeroes
print("Part 1:",part1)

image = ["2" for _ in range(len(layers[0]))]
for layer in layers:
    for i in range(len(image)):
        if image[i] == "2" and layer[i] != "2":
            image[i] = layer[i]

print("Part 2:")
for line in range(l):
    print("".join(image[w*line : w*line+w]).replace("0"," "))