def solve(expand_factor):
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    empty_cols = [c for c in range(len(lines[0])) if len(set([val[c] for val in lines])) == 1]
    empty_rows = [r for r in range(len(lines)) if len(set(lines[r])) == 1]
    points = []
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] == "#":
                points.append( (r + sum(expand_factor for e in empty_rows if e<r),c + sum(expand_factor for e in empty_cols if e<c)) )
    sum1 = 0
    for i in range(len(points)-1):
        for j in range(i+1,len(points)):
            p1,p2 = points[i],points[j]
            sum1 += abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    return sum1

if __name__ == "__main__":
    print("Part 1:",solve(1))
    print("Part 2:",solve(1000000-1))