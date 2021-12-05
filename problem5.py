def solve(part1):
    f = open("input5.txt")
    # TODO: still using hardcoded max so I don't have to iterate through the list again, or grow as I build
    pointMap = [[0 for i in range(1000)] for j in range(1000)]
    for line in f:
        points = line.split(" -> ")
        x1, y1, x2, y2 = list(map(int, points[0].split(",") + points[1].split(",")))
        if x1 == x2:
            for y in range(min(y1,y2),max(y1,y2)+1):
                pointMap[x1][y] += 1
        elif y1 == y2:
            for x in range(min(x1,x2),max(x1,x2)+1):
                pointMap[x][y1] += 1
        elif part1:
            y = y1 if x1 < x2 else y2
            for x in range(min(x1,x2),max(x1,x2)+1):
                pointMap[x][y] += 1
                y += 1 if ((y2 > y1 and x1 < x2) or (y2 < y1 and x1 > x2)) else -1
    answer = 0
    for x in pointMap:
        for y in x:
            answer += 1 if y > 1 else 0
    return answer

print("Part 1:", solve(False))
print("Part 2:", solve(True))