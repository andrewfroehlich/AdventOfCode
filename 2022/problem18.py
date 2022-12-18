from collections import deque

def build_cubes(file):
    cubes = set()
    for line in open(file).read().splitlines(): 
        cubes.add( tuple([int(d) for d in line.split(",")]) )
    return cubes

def part1(cubes):
    part1 = 0
    for cube in cubes:
        part1 += 6# - find_adjacent_count(cube,cubes)
        x,y,z = cube
        for a,b,c in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
            if (x+a,y+b,z+c) in cubes:
                part1 -= 1
    return part1

def part2(cubes):
    min_x,max_x = min(cubes,key=lambda item:item[0])[0]-1, max(cubes,key=lambda item:item[0])[0]+1
    min_y,max_y = min(cubes,key=lambda item:item[1])[1]-1, max(cubes,key=lambda item:item[1])[1]+1
    min_z,max_z = min(cubes,key=lambda item:item[2])[2]-1, max(cubes,key=lambda item:item[2])[2]+1
    bfs = deque([ (min_x,min_y,min_z) ])
    visited = set([ (min_x,min_y,min_z) ])
    part2 = 0
    while bfs:
        x,y,z = bfs.popleft()
        for a,b,c in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
            if (x+a,y+b,z+c) in cubes:
                part2 += 1
            elif min_x<=x+a<=max_x and min_y<=y+b<=max_y and min_z<=z+c<=max_z and (x+a,y+b,z+c) not in visited:
                visited.add( (x+a,y+b,z+c) )
                bfs.append( (x+a,y+b,z+c) )
    return part2

cubes = build_cubes("input18.txt")
print("Part 1:",part1(cubes))
print("Part 2:",part2(cubes))