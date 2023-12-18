from collections import deque

def part1():
    direct = {"U":(0,-1),"R":(1,0),"L":(-1,0),"D":(0,1)}
    m = set()
    x,y = 0,0
    x_range,y_range = [0,0],[0,0]
    
    # create set of points, updating the range
    for line in open("input.txt"):
        d,n,_ = line.strip().split()
        i,j = direct[d]
        for _ in range(int(n)):
            x,y = x+i,y+j
            m.add((x,y))
        x_range = [min(x_range[0],x),max(x_range[1],x)]
        y_range = [min(y_range[0],y),max(y_range[1],y)]
        
    # bfs outside of the area to count the points we can't reach
    bfs = deque( [(x_range[0]-1,y_range[0]-1)] )
    visited = set()
    count = 0
    while bfs:
        x,y = bfs.popleft()
        if (x,y) in visited:
            continue
        visited.add( (x,y) )
        count += 1
        for i,j in direct.values():
            if (x+i,y+j) not in m and x_range[0]-1 <= x+i <= x_range[1]+1 and y_range[0]-1 <= y+j <= y_range[1]+1:
                bfs.append( (x+i,y+j) )
    return ((x_range[1]+1)-(x_range[0]-1)+1)*((y_range[1]+1)-(y_range[0]-1)+1) - count

def part2():
    direct = [(1,0),(0,1),(-1,0),(0,-1)] # "0 means R, 1 means D, 2 means L, and 3 means U"
    current = (0,0)
    exterior_pts, shoelace_sum = 0, 0
    # Shoelace Theorem for Area using cross-products, Pick's Theorem to get interior points to add to exterior
    for line in open("input.txt"):
        color = line.strip().split("#")[1][:-1]
        steps = int(color[:-1],16)
        d = direct[int(color[-1])]
        i,j = steps*d[0],steps*d[1]
        x,y = current
        shoelace_sum += (y+j)*x - (x+i)*y
        exterior_pts += steps
        current = (x+i,y+j)
    return abs(shoelace_sum // 2) + 1 - ((exterior_pts) // 2) + exterior_pts

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())