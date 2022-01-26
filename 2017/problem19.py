lines = open("Resources/input19.txt").readlines()
tubes = dict()
x = y = 0
for l in range(len(lines)):
    for c in range(len(lines[l])):
        ch = lines[l][c]
        if ch.strip():
            tubes[(c,l)] = ch
            if l == 0:
                x,y = c,l

adjacency = [(0,1),(0,-1),(1,0),(-1,0)]
direction = (0,1)
steps = 1
path = []
while True:
    x,y = x+direction[0],y+direction[1]
    if (x,y) not in tubes:
        break
    steps += 1
    ch = tubes[(x,y)]
    if ch.isalpha():
        path.append(ch)
    elif ch == "+":
        paths = list(filter(lambda coord: coord not in (direction, (-direction[0],-direction[1])), adjacency))
        for a,b in paths:
            if (x+a, y+b) in tubes and (
                (a!=0 and tubes[(x+a,y+b)] != "|") or (b!=0 and tubes[(x+a,y+b)] != "-")):
                direction = (a,b)
print("Part 1:","".join(path),"\nPart 2:",steps) #16643 too high