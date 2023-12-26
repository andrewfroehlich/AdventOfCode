import z3
import re

def parse_file():
    return [tuple([int(d) for d in re.split(',|@',line)]) for line in open("input.txt")]

def make_2d_lines(pt_and_slopes):
    lines = []
    for x,y,_,dx,dy,_ in pt_and_slopes:
        x2,y2 = x+dx,y+dy # make a second point at time = 1
        lines.append( (y-y2, x2-x, -1*(x*y2-x2*y)) )
    return lines

def intersection(l1, l2):
    a1,b1,c1 = l1
    a2,b2,c2 = l2
    d = a1*b2 - b1*a2
    return None if d==0 else ((c1*b2 - b1*c2)/d, (a1*c2 - c1*a2)/d)

def part1(min_val, max_val):
    pt_and_slopes = parse_file()
    lines = make_2d_lines(pt_and_slopes)
    sum1 = 0
    for i in range(len(lines)-1):
        for j in range(i+1,len(lines)):
            pt = intersection(lines[i],lines[j])
            if pt and min_val<=pt[0]<=max_val and min_val<=pt[1]<=max_val:
                x,y = pt
                x1,y1,_,dx1,dy1,_ = pt_and_slopes[i]
                x2,y2,_,dx2,dy2,_ = pt_and_slopes[j]
                if (x-x1)*dx1 > 0 and (x-x2)*dx2 > 0 and (y-y1)*dy1 > 0 and (y-y2)*dy2 > 0:
                    sum1 += 1
    return sum1

def part2():
    pt_and_slopes = parse_file()
    rpx,rpy,rpz,rdx,rdy,rdz = z3.Ints("rpx rpy rpz rdx rdy rdz") # rock position and slope
    solve = z3.Solver()
    for i in range(3): # only need 3 hailstones to complete the equations
        x,y,z,dx,dy,dz = pt_and_slopes[i]
        t_i = z3.Int("t"+str(i)) # collision time of the rock and this hailstone
        solve.add(t_i > 0)
        solve.add(rpx + t_i*rdx == x + t_i*dx)
        solve.add(rpy + t_i*rdy == y + t_i*dy)
        solve.add(rpz + t_i*rdz == z + t_i*dz)
    solve.check()
    return sum(solve.model()[var].as_long() for var in [rpx,rpy,rpz])
    
if __name__ == "__main__":
    print("Part 1:", part1(200000000000000,400000000000000))
    print("Part 2:", part2())