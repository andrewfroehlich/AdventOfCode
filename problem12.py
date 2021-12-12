from collections import defaultdict

f = open("input12.txt")
edges = defaultdict(list)
for line in f:
    points = line.strip().split('-')
    if points[0] != "end" and points[1] != "start": #nothing toward start or from end
        edges[points[0]].append(points[1])
    if points[1] != "end" and points[0] != "start": #nothing toward start or from end
        edges[points[1]].append(points[0])

def traverse(current, visited, revisited):
    if current.islower():
        visited.add(current) #only 'visit' if on a small cave
    if current == "end":
        global paths
        paths += 1
    else:
        for point in edges[current]:
            if point not in visited:
                traverse(point, visited.copy(), revisited)
            elif not revisited: #can still revisit once
                traverse(point, visited.copy(), True)

paths = 0
traverse("start", set(), True)
print("Part 1:",paths)
paths = 0
traverse("start", set(), False)
print("Part 2:",paths)