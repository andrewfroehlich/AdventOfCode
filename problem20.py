enh,img = open("input20.txt").read().strip().split('\n\n')
image = set()
imageLines = img.split("\n")
for i in range(len(imageLines)):
    for j in range(len(imageLines[i])):
        if imageLines[i][j] == '#':
            image.add((i,j))
binary_mask = [(1,1),(1,0),(1,-1),(0,1),(0,0),(0,-1),(-1,1),(-1,0),(-1,-1)]
x_range = (0,len(imageLines))
y_range = (0, len(imageLines[0]))
steps = 1
while steps <= 50:
    new_image = set()
    for x in range(x_range[0]-5-steps, x_range[1]+5+steps):
        for y in range(y_range[0]-5-steps, y_range[1]+5+steps):
            enh_value = 0
            for b in range(len(binary_mask)):
                if (x+binary_mask[b][0],y+binary_mask[b][1]) in image:
                    enh_value += 2**b
            if enh[enh_value] == '#' and not (steps % 2 == 0 and enh[0] == "#" and (x < x_range[0]-2-steps or x > x_range[1]+2+steps or y < y_range[0]-2-steps or y > y_range[1]+2+steps)):
                new_image.add((x,y))
    image = new_image.copy()
    if steps == 2:
        print("Part 1:",len(image))
    steps += 1
print("Part 2:",len(image))