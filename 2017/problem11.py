"""
  sw  nw
s   00   n
  se  ne

-2: -1 0 1 2 3 4 5
-1:-1 0 1 2 3 4 5 
 0: -1 0 1 2 3 4 5
 1:-1 0 1 2 3 4 5
"""

def steps(x,y):
    steps = 0
    while x != 0 and y != 0:
        steps += 1
        if x < 0:
            if y < 0:
                if y % 2 == 0:
                    x += 1
                y += 1
            else:
                if y % 2 == 0:
                    x += 1
                y -= 1
        else:
            if y < 0:
                if y % 2 == 1:
                    x -= 1
                y += 1
            else:
                if y % 2 == 1:
                    x -= 1
                y -= 1
    return steps+abs(x)+abs(y)
 
x = y = part2 = 0
part2coord = (0,0)
for step in open("Resources/input11.txt").readline().strip().split(","):
    if step == "n":
        x += 1
    elif step == "s":
        x -= 1
    elif step == "nw":
        if y % 2 == 0:
            x += 1
        y -= 1
    elif step == "sw":
        if y % 2 == 1:
            x -= 1
        y -= 1
    elif step == "ne":
        if y % 2 == 0:
            x += 1
        y += 1
    else: #"se"
        if y % 2 == 1:
            x -= 1
        y += 1
    if (abs(x) + abs(y)/2) > part2:
        part2 = (abs(x) + abs(y)/2)
        part2coord = (x,y)

print("Part 1:",steps(x,y))
print("Part 2:",steps(part2coord[0],part2coord[1]))