x = y = 0
directions = [(0,1),(1,0),(0,-1),(-1,0)]
facing_i = 0
visited = set((x,y))
part2 = -1
for instruction in open("Resources/input1.txt").readline().strip().split(", "):
    turn = instruction[0:1]
    val = int(instruction[1:])
    facing_i = ((facing_i + 1 if turn == "R" else facing_i - 1) + 4) % 4
    for _ in range(val):
        x += directions[facing_i][0]
        y += directions[facing_i][1]
        if part2 == -1 and (x,y) in visited:
            part2 = x+y
        visited.add( (x,y) )
print("Part 1:",x+y,"\nPart 2:",part2)