def find_in_multi_array(lines,symbol):
    for j in range(len(lines)):
        for i in range(len(lines[j])):
            if lines[j][i] == symbol:
                return (i,j)

def part1(lines):
    s = find_in_multi_array(lines,"S")
    p2_map = {}
    adjacency = {".":[],"-":[(-1,0),(1,0)],"|":[(0,-1),(0,1)],
                 "7":[(-1,0),(0,1)],"F":[(1,0),(0,1)],
                 "J":[(-1,0),(0,-1)],"L":[(1,0),(0,-1)]}
    opp = {(1,0):(-1,0), (0,1):(0,-1), (-1,0):(1,0), (0,-1):(0,1)}
    
    c1,c2,last1,last2 = (0,0,0,0) # counter coords and last move taken e.g. (0,1)
    for i,j in [(-1,0),(0,1),(1,0),(0,-1)]:
        adj_check = (s[0]+i,s[1]+j)
        sym = lines[adj_check[1]][adj_check[0]]
        if opp[(i,j)] in adjacency[sym]: # if adjacent block connects
            if c1 == 0:
                c1 = adj_check
                last1 = (i,j)
            else:
                c2 = adj_check
                last2 = (i,j)
            p2_map[adj_check] = sym
    steps = 1
    for key,val in adjacency.items():
        if set(val) == set([last1,last2]):
            p2_map[s] = key # set the map to the correct pipe value for S coordinate
    
    while c1 != c2: # step around the circle until the points meet
        c1,last1 = advance(c1,last1,lines,adjacency,opp)
        p2_map[c1] = lines[c1[1]][c1[0]]
        if c1 == c2:
            return steps,p2_map
        c2,last2 = advance(c2,last2,lines,adjacency,opp)
        p2_map[c2] = lines[c2[1]][c2[0]]
        steps += 1
    return steps,p2_map

def advance(c,last,lines,adjacency,opp):
    adj = adjacency[lines[c[1]][c[0]]]
    next_move = adj[1] if adj[0] == opp[last] else adj[0]
    return (c[0]+next_move[0],c[1]+next_move[1]),next_move

def part2(lines,pipe_map):
    corners = {"7":[(-1,0),(0,1)], "F":[(1,0),(0,1)], "J":[(-1,0),(0,-1)], "L":[(1,0),(0,-1)]}
    sum2 = 0
    for j in range(len(lines)):
        for i in range(len(lines[j])):
            if (i,j) not in pipe_map:
                if count_edges(pipe_map,corners,i+1,len(lines[j]),1,True,j) % 2 == 0:
                    continue
                if count_edges(pipe_map,corners,i-1,-1,-1,True,j) % 2 == 0:
                    continue
                if count_edges(pipe_map,corners,j+1,len(lines),1,False,i) % 2 == 0:
                    continue
                if count_edges(pipe_map,corners,j-1,-1,-1,False,i) % 2 == 0:
                    continue
                sum2 += 1
    return sum2

def count_edges(pipe_map,corners,range_start,range_end,range_step,horiz_flag,static):
    intersections = 0
    corner_open = None
    counted_line = "|" if horiz_flag else "-"
    not_counted_line = "-" if horiz_flag else "|"
    plane_cross = [(0,1),(0,-1)] if horiz_flag else [(1,0),(-1,0)]
    for x in range(range_start,range_end,range_step):
        point = (x,static) if horiz_flag else (static,x)
        if point in pipe_map and pipe_map[point] == counted_line:
            intersections += 1
        elif point in pipe_map and pipe_map[point] != not_counted_line:
            if corner_open is not None:
                # only count as an intersection if the pipe crosses the plane
                if (plane_cross[0] in corners[corner_open] or plane_cross[0] in corners[pipe_map[point]]) and \
                        (plane_cross[1] in corners[corner_open] or plane_cross[1] in corners[pipe_map[point]]):
                    intersections += 1
                corner_open = None
            else:
                corner_open = pipe_map[point]
    return intersections

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    p1,p2_map = part1(lines)
    print("Part 1:",p1)
    print("Part 2:",part2(lines,p2_map))