def solve(part):
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    exp_factor = 1 if part == 1 else (1000000-1)
    exp_cols = [c for c in range(len(lines[0])) if len(set([val[c] for val in lines])) == 1]
    points = []
    row = 0
    for r in lines:
        found = False
        for c in range(len(r)):
            if r[c] =="#":
                points.append( (row,c + sum(exp_factor for e in exp_cols if e<c)) )
                found = True
        row = row+1 if found else row+1+exp_factor
    
    sum1 = 0
    for i in range(len(points)-1):
        for j in range(i+1,len(points)):
            p1,p2 = points[i],points[j]
            sum1 += abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    return sum1

if __name__ == "__main__":
    print("Part 1:",solve(1))
    print("Part 2:",solve(2))