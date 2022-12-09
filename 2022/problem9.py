def inc(head, tail):
    return tail+1 if head > tail else tail-1

def execute(knot_count):
    knots = [(0,0) for _ in range(knot_count)]
    movement = {"U":(-1,0), "D":(1,0), "R":(0,1), "L":(0,-1)}
    visited = set() #tracks only the tail knot
    visited.add( knots[-1] )
    for line in open("input9.txt"):
        direction,steps = line.split()
        inc_x,inc_y = movement[direction]
        for i in range(int(steps)):
            head_x,head_y = knots[0]
            knots[0] = (head_x+inc_x, head_y+inc_y)
            for knot_i in range(1,len(knots)):
                knot_x,knot_y = knots[knot_i]
                lead_x,lead_y = knots[knot_i-1]
                if abs(lead_x - knot_x) > 1 or abs(lead_y - knot_y) > 1:
                    if lead_x == knot_x:
                        knot_y = inc(lead_y,knot_y)
                    elif lead_y == knot_y:
                        knot_x = inc(lead_x,knot_x)
                    else: #diagonal
                        knot_x = inc(lead_x,knot_x)
                        knot_y = inc(lead_y,knot_y)
                knots[knot_i] = (knot_x,knot_y)
                if knot_i == len(knots)-1:
                    visited.add( (knot_x,knot_y) )
    return len(visited)

print("Part 1:",execute(2))
print("Part 2:",execute(10))