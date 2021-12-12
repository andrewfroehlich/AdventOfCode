from collections import defaultdict

f = open("input12.txt")
edges = defaultdict(list)
for line in f:
    points = line.strip().split('-')
    if points[1] != "start" and points[0] != "end":
        edges[points[0]].append(points[1])
    if points[0] != "start" and points[1] != "end":
        edges[points[1]].append(points[0])

def traverse(current, visited, smallCaveRevisited):
    if not current[0].isupper():
        visited.add(current) #only say visited if small cave
    if current == "end":
        global paths
        paths += 1
    else:
        for point in edges[current]:
            if point not in visited:
                traverse(point, visited.copy(), smallCaveRevisited)
            elif not smallCaveRevisited:
                traverse(point, visited.copy(), True)

paths = 0
traverse("start", set(), True)
print("Part 1:",paths)
paths = 0
traverse("start", set(), False)
print("Part 2:",paths)