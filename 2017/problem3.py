import math

target = 361527
next_corner_i = math.ceil(math.sqrt(target))
if next_corner_i % 2 == 0:
    next_corner_i += 1
next_corner = next_corner_i ** 2
prev_corner = (next_corner_i-2) ** 2
side_len = (next_corner-prev_corner)//4
current = next_corner
distance = next_corner_i-1

for _ in range(4):
    if current == target:
        break
    for i in range(side_len):
        if i < side_len//2:
            distance -= 1
        else:
            distance += 1
        current -= 1
        if current == target:
            break
print("Part 1:",distance)

adj_order = [(1,0),(0,1),(-1,0),(0,-1)]
neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
grid = dict()
x = y = dir_index = 0
grid[(x,y)] = 1
last_val = 1
while last_val <= target:
    x,y = x+adj_order[dir_index][0],y+adj_order[dir_index][1]
    last_val = 0
    for a,b in neighbors:
        if (x+a,y+b) in grid:
            last_val += grid[(x+a,y+b)]
    grid[(x,y)] = last_val
    if (x+adj_order[(dir_index+1)%4][0],y+adj_order[(dir_index+1)%4][1]) not in grid:
        dir_index = (dir_index+1)%4
print("Part 2:",last_val)