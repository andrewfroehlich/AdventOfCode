lines = []
for line in open("input8.txt"):
    lines.append(line.strip())

visible = set()
for i in range(len(lines)):
    max_found = -1
    for j in range(len(lines[i])):
        if int(lines[i][j]) > max_found:
            visible.add( (i,j) )
            max_found = int(lines[i][j])
    max_found = -1
    for j in range(len(lines[i])-1,-1,-1):
        if int(lines[i][j]) > max_found:
            visible.add( (i,j) )
            max_found = int(lines[i][j])
for j in range(len(lines[0])):
    max_found = -1
    for i in range(len(lines)):
        if int(lines[i][j]) > max_found:
            visible.add( (i,j) )
            max_found = int(lines[i][j])
    max_found = -1
    for i in range(len(lines)-1,-1,-1):
        if int(lines[i][j]) > max_found:
            visible.add( (i,j) )
            max_found = int(lines[i][j])
print("Part 1:",len(visible))

max_view_score = -1
directions = [(0,1),(0,-1),(1,0),(-1,0)]
for i in range(len(lines)):
    for j in range(len(lines[0])):
        current_tree = int(lines[i][j])
        current_view_score = 1
        for x,y in directions:
            trees_seen = 0
            a,b = i+x,j+y
            halt = False
            while 0 <= a < len(lines) and 0 <= b < len(lines[0]) and not halt:
                trees_seen += 1
                if int(lines[a][b]) >= current_tree:
                    halt = True
                a,b = a+x,b+y
            current_view_score = current_view_score * trees_seen
        max_view_score = max(max_view_score,current_view_score)
print("Part 2:",max_view_score)