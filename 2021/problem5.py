def addPoint(point, points, overlaps):
    if point in points:
        overlaps.add(point)
    points.add(point)

def solve(part1):
    f = open("input5.txt")
    pointMap = set()
    overlapMap = set()
    for line in f:
        points = line.split(" -> ")
        x1, y1, x2, y2 = list(map(int, points[0].split(",") + points[1].split(",")))
        if x1 == x2:
            for y in range(min(y1,y2),max(y1,y2)+1):
                addPoint((x1,y), pointMap, overlapMap)
        elif y1 == y2:
            for x in range(min(x1,x2),max(x1,x2)+1):
                addPoint((x,y1), pointMap, overlapMap)
        elif part1:
            y = y1 if x1 < x2 else y2
            for x in range(min(x1,x2),max(x1,x2)+1):
                addPoint((x,y), pointMap, overlapMap)
                y += 1 if ((y2 > y1 and x1 < x2) or (y2 < y1 and x1 > x2)) else -1
    return len(overlapMap)

print("Part 1:", solve(False))
print("Part 2:", solve(True))