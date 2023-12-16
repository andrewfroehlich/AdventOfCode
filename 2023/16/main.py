from collections import deque

def parseFile():
    lines = open("input.txt").read().splitlines()
    mirrors = dict()
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] != ".":
                mirrors[(x,y)] = lines[y][x]
    return mirrors, len(lines[0]), len(lines)

def solve():
    mirrors,max_x,max_y = parseFile()
    direct = {"|":{(1,0):[(0,1),(0,-1)],(-1,0):[(0,1),(0,-1)],(0,1):[(0,1)],(0,-1):[(0,-1)]},
              "-":{(0,1):[(1,0),(-1,0)],(0,-1):[(1,0),(-1,0)],(1,0):[(1,0)],(-1,0):[(-1,0)]},
              "/":{(1,0):[(0,-1)],(-1,0):[(0,1)],(0,1):[(-1,0)],(0,-1):[(1,0)]},
              "\\":{(1,0):[(0,1)],(-1,0):[(0,-1)],(0,1):[(1,0)],(0,-1):[(-1,0)]}}
    context = (mirrors,direct,max_x,max_y)
    p1 = p2_max = run_bfs((0,0),(1,0),context)
    for x in range(max_x):
        p2_max = max(p2_max, run_bfs((x,0),(0,1),context), run_bfs((x,max_y-1),(0,-1),context))
    for y in range(max_y):
        p2_max = max(p2_max, run_bfs((0,y),(1,0),context), run_bfs((max_x-1,y),(-1,0),context))
    return p1,p2_max

def run_bfs(first_pt, first_dir, context):
    mirrors, direct, max_x, max_y = context
    lit,seen = set(),set()
    bfs = deque()
    bfs.append( (first_pt,first_dir) )
    while bfs:
        c_pt, c_dir = bfs.popleft()
        if (c_pt,c_dir) in seen or not (0 <= c_pt[0] < max_x) or not (0 <= c_pt[1] < max_y):
            continue # don't continue if we've processed this point+direction before or we're out of the grid
        seen.add( (c_pt,c_dir) )
        lit.add(c_pt)
        if c_pt in mirrors: 
            for i,j in direct[mirrors[c_pt]][c_dir]:
                bfs.append( ((c_pt[0]+i,c_pt[1]+j), (i,j)) )
        else:
            bfs.append( ((c_pt[0]+c_dir[0],c_pt[1]+c_dir[1]), c_dir) )
    return len(lit)

if __name__ == "__main__":
    p1,p2 = solve()
    print("Part 1:",p1)
    print("Part 2:",p2)