def safe_access(grid, i, j):
    if 0 <= i < len(grid) and 0 <= j < len(grid[i]):
        return grid[i][j]
    else:
        return "."

def part1(grid):
    part1 = 0
    dirs = [(-1,0),(-1,-1),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "X":
                for x,y in dirs:
                    if ''.join(safe_access(grid, i + x*z, j + y*z) for z in range(4)) == "XMAS":
                        part1 += 1
    return part1

def part2(grid):
    part2 = 0
    dirs = [(-1,-1),(-1,1),(1,1),(1,-1)]
    targets = set(["MSSM","SSMM","SMMS","MMSS"])
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "A":
                if ''.join(safe_access(grid, i+x, j+y) for x,y in dirs) in targets:
                    part2 += 1
    return part2

if __name__ == "__main__":
    grid = open("input.txt").read().splitlines()
    print("Part 1:",part1(grid))
    print("Part 2:",part2(grid))