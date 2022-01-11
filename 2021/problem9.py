def part1():
    with open("input9.txt") as f:
        lines = f.read().splitlines()
    answer = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            value = int(lines[i][j])
            if (i == 0 or int(lines[i-1][j]) > value) and \
              (i == len(lines)-1 or int(lines[i+1][j]) > value) and \
              (j == 0 or int(lines[i][j-1]) > value) and \
              (j == len(lines[i])-1 or int(lines[i][j+1]) > value):
                answer += 1 + value
    return answer

def part2():
    with open("input9.txt") as f:
        lines = f.read().splitlines()
    seen = set()
    
    def area(x,y):
        if x<0 or x>=len(lines) or y<0 or y>=len(lines[x]) or \
          ((x,y) in seen) or lines[x][y] == "9":
            return 0
        seen.add((x,y))
        return 1 + area(x+1,y) + area(x-1,y) + area(x,y-1) + area(x,y+1)
    
    islandSizes = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            islandSize = area(i,j)
            if(islandSize > 0):
                islandSizes.append(islandSize)
    islandSizes.sort()
    return islandSizes[-1]*islandSizes[-2]*islandSizes[-3]

print("Part 1:",part1())
print("Part 2:",part2())