def horizontal(p,smudge_target):
    for r in range(1,len(p)): # iterate over possible rows of reflection
        smudges_found = 0
        for i in range(0,min(len(p)-r,r)): # iterate in both directions away from that row of reflection
            for j in range(len(p[0])): # for each line, check equality character by character for accurate smudge count
                smudges_found += 1 if p[r+i][j] != p[r-i-1][j] else 0
                if smudges_found > smudge_target:
                    break
        if smudges_found == smudge_target:
            return r
    return 0

def vertical(p,smudge_target):
    pivot = [[row[i] for row in p] for i in range(len(p[0]))]
    return horizontal(pivot,smudge_target)

def solve(patterns,smudge_target):
    return sum([vertical(p,smudge_target)+100*horizontal(p,smudge_target) for p in patterns])
    
if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        sections = f.read().split("\n\n")
    patterns = [line.split("\n") for line in sections]
    print("Part 1:",solve(patterns,0))
    print("Part 2:",solve(patterns,1))