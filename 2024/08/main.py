from collections import defaultdict
from itertools import combinations
from math import gcd

def part1_antinodes(p1,p2,max_x,max_y):
    points = set()
    x1, y1 = p1
    x2, y2 = p2
    dx,dy = x2 - x1,y2 - y1
    x,y = x2 + (x2-x1), y2 + (y2-y1)
    if 0 <= x <= max_x and 0 <= y <= max_y:
        points.add( (x,y) )
    x,y = x1 + (x1-x2), y1 + (y1-y2)
    if 0 <= x <= max_x and 0 <= y <= max_y:
        points.add( (x,y) )
    return points

def part2_antinodes(p1,p2,max_x,max_y):
    points = set()
    x1, y1 = p1
    x2, y2 = p2
    dx,dy = x2 - x1,y2 - y1
    g = gcd(dx, dy)
    step_x,step_y = dx // g,dy // g

    return set([(x, y) for t in range(-max_x, max_x)
        if 0 <= (x := x1 + t * step_x) <= max_x
        and 0 <= (y := y1 + t * step_y) <= max_y])

def process_input():
    grid = open("input.txt").read().splitlines()
    ant = defaultdict(set)
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if grid[j][i] != ".":
                ant[grid[j][i]].add( (i,j) )
    return ant,len(grid[0])-1,len(grid)-1

def run(ant,max_x,max_y,is_part2):
    anti_nodes = set()
    for locations in ant.values():
        if len(locations) == 1:
            continue #no anti-nodes with only one antenna of that frequency
        for combo in combinations(locations,2):
            ant1,ant2 = combo
            new_anti_nodes = part2_antinodes(ant1,ant2,max_x,max_y) if is_part2 else part1_antinodes(ant1,ant2,max_x,max_y)
            anti_nodes.update(new_anti_nodes)
    return len(anti_nodes)

if __name__ == "__main__":
    ant,max_x,max_y = process_input()
    print("Part 1:",run(ant,max_x,max_y,False))
    print("Part 2:",run(ant,max_x,max_y,True))