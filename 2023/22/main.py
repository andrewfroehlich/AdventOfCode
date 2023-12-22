import re
from collections import defaultdict, deque
from heapq import heappush, heappop

def drop_bricks():
    m, k_supports_v, k_supported_by_v = dict(), defaultdict(set), defaultdict(set)
    
    # parse bricks, ordering by min z value
    bricks = []
    for line in open("input.txt"):
        x1,y1,z1,x2,y2,z2 = [int(d) for d in re.split(',|~',line)]
        heappush(bricks, (min(z1,z2),x1,y1,z1,x2,y2,z2,len(bricks)+1))
    total_bricks = len(bricks)
        
    while bricks:
        # drop brick until it hits another brick (in map m) or floor (z=0)
        _,x1,y1,z1,x2,y2,z2,brick = heappop(bricks)
        brick_pts = [(x,y,z) for x in range(x1,x2+1) for y in range(y1,y2+1) for z in range(z1,z2+1)]
        while True:
            new_brick_pts = [(x,y,z-1) for x,y,z in brick_pts]
            supporting_bricks = set([m[(x,y,z)] for x,y,z in new_brick_pts if (x,y,z) in m])
            if supporting_bricks or any([1 for _,_,z in new_brick_pts if z == 0]):
                break
            brick_pts = new_brick_pts
        
        # brick has settled, fill dictionaries with brick information
        for x,y,z in brick_pts:
            m[(x,y,z)] = brick
        k_supported_by_v[brick] = supporting_bricks
        for supporting_brick in supporting_bricks:
            k_supports_v[supporting_brick].add(brick)
    return k_supports_v, k_supported_by_v, total_bricks

def part1(k_supports_v, k_supported_by_v, total_bricks):
    # count each brick only if all of those supported by it (if existing) have other supports
    return sum(all([len(k_supported_by_v[b2])!=1 for b2 in k_supports_v[b]]) for b in range(1,total_bricks+1))

def part2(k_supports_v, k_supported_by_v, total_bricks):
    sum2 = 0
    for b in range(1,total_bricks+1):
        bricks_moved = set([b])
        bfs = deque( list(k_supports_v[b]) )
        while bfs:
            current = bfs.popleft()
            if not all([n in bricks_moved for n in k_supported_by_v[current]]):
                continue # if all supports of the current haven't moved, stop
            bricks_moved.add(current)
            bfs.extend(k_supports_v[current]) # add everything this supports to the end
        sum2 += len(bricks_moved) - 1 # don't count yourself
    return sum2

if __name__ == "__main__":
    context = drop_bricks()
    print("Part 1:",part1(*context))
    print("Part 2:",part2(*context))