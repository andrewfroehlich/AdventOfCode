from collections import deque

def elevation(c):
    if c == 'S':
        return ord('a')
    elif c == 'E':
        return ord('z')
    return ord(c)

lines = open("input12.txt").read().splitlines()
end = (-1,-1)
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "E":
            end = (i,j)
            break
    if end != (-1,-1):
        break

directions = [(-1,0),(0,1),(0,-1),(1,0)]
bfs = deque( [(end[0], end[1], 0)] )
visited = set( [(end[0], end[1])] )
part2 = -1
while len(bfs) > 0:
    i, j, steps = bfs.popleft()
    if part2 == -1 and (lines[i][j] == 'a' or lines[i][j] == 'S'):
        part2 = steps
    if lines[i][j] == 'S':
        print("Part 1:",steps)
        break
    for x,y in directions:
        if 0 <= i+x < len(lines) and 0 <= j+y < len(lines[0]) and (i+x,j+y) not in visited and elevation(lines[i+x][j+y])+1 >= elevation(lines[i][j]):
            visited.add( (i+x, j+y) )
            bfs.append( (i+x, j+y, steps+1) )

print("Part 2:",part2)