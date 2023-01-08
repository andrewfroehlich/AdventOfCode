from collections import defaultdict
from collections import deque

def build_maps():
    raw_data = open("Resources/input6.txt").read().splitlines()
    orbiters,orbited = defaultdict(list),defaultdict(list)
    for line in raw_data:
        spl = line.split(")")
        orbiters[spl[0]].append(spl[1])
        orbited[spl[1]].append(spl[0])
    return orbiters,orbited

def part1(orbiters):
    bfs = deque()
    bfs.append( ("COM",1) ) #node, depth
    part1 = 0
    while bfs:
        current,depth = bfs.popleft()
        orb = orbiters[current]
        for o in orb:
            part1 += depth
            bfs.append( (o,depth+1) )
    return part1

def part2(orbited,orbiters):
    bfs,visited = deque(),set()
    targets = set(orbited["SAN"])
    bfs.append( ("YOU",-1) ) #current, steps
    visited.add("YOU")
    while bfs:
        current,steps = bfs.popleft()
        if current in targets:
            return steps

        for o in orbiters[current]:
            if o not in visited:
                visited.add(o)
                bfs.append( (o, steps+1) )
        for o in orbited[current]:
            if o not in visited:
                visited.add(o)
                bfs.append( (o, steps+1) )

orbiters,orbited = build_maps()
print("Part 1:",part1(orbiters))
print("Part 2:",part2(orbited,orbiters))