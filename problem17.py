import math

f_input = open("input17.txt").read().split(", ")
x_range = (int(f_input[0].split("..")[0].split('=')[1]),int(f_input[0].split("..")[1]))
y_range = (int(f_input[1].split("..")[0].split('=')[1]),int(f_input[1].split("..")[1]))
minX = math.ceil((-1 + math.sqrt(1 + 4*(2*x_range[0])))/2) #quadratic formula, solving for n(n+1)/2 = x
maxX = x_range[1]
minY = y_range[0]
maxY = abs(y_range[0])-1
print("Part 1:",minY*(minY+1)//2)

part2 = 0
for x in range(minX,maxX+1):
    for y in range(minY, maxY+1):
        current_x,current_y = x,y
        coordX = coordY = 0
        while coordX <= x_range[1] and coordY >= y_range[0]:
            if coordX >= x_range[0] and coordY <= y_range[1]:
                part2 += 1
                break
            else:
                coordX += current_x
                coordY += current_y
                if current_x > 0: current_x -= 1
                current_y -= 1
print("Part 2:",part2)