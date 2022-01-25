#from collections import defaultdict
from collections import deque

def BFS(start, d):
    global visited
    stack = deque()
    stack.append(start)
    while stack:
        current = stack.popleft()
        visited.add(current)
        for dst in d[current]:
            if dst not in visited:
                stack.append(dst)

d = dict()
max_src = 0
for line in open("Resources/input12.txt"):
    src,dest_list = line.strip().split(" <-> ")
    d[int(src)] = [int(j) for j in dest_list.split(", ")]
    max_src = max(max_src,int(src))
visited = set()
BFS(0,d)
print("Part 1:",len(visited))

groups = 1
for i in range(max_src):
    if i not in visited:
        BFS(i,d)
        groups += 1
print("Part 2:",groups)
