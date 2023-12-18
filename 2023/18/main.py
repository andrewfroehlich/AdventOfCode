from collections import deque

def part1():
    direct = {"U":(0,-1),"R":(1,0),"L":(-1,0),"D":(0,1)}
    directions = []
    for line in open("input.txt"):
        d,n,_ = line.strip().split()
        i,j = direct[d]
        directions.append( (int(n),direct[d]) )
    return shoelace_pick(directions)
    
def part2():
    direct = [(1,0),(0,1),(-1,0),(0,-1)] # "0 means R, 1 means D, 2 means L, and 3 means U"
    directions = []
    for line in open("input.txt"):
        code = line.strip().split("#")[1][:-1]
        steps = int(code[:-1],16)
        d = direct[int(code[-1])]
        directions.append( (steps,d) )
    return shoelace_pick(directions)

def shoelace_pick(directions):
    current = (0,0)
    exterior_pts, shoelace_sum = 0, 0
    # Shoelace Theorem for Area using cross-products, Pick's Theorem to get interior points to add to exterior
    for steps,d in directions:
        i,j = steps*d[0],steps*d[1]
        x,y = current
        shoelace_sum += (y+j)*x - (x+i)*y
        exterior_pts += steps
        current = (x+i,y+j)
    return abs(shoelace_sum // 2) + 1 - (exterior_pts // 2) + exterior_pts

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())