from collections import defaultdict

f = open("input13.txt")
xtoy = defaultdict(set)
ytox = defaultdict(set)
maxX = maxY = 0
folds = []
parseFolds = False
for line in f:
    if line.strip() == "":
        parseFolds = True
    elif not parseFolds:
        coord = line.strip().split(',')
        x = int(coord[0])
        y = int(coord[1])
        maxX = x if x > maxX else maxX
        maxY = y if y > maxY else maxY
        xtoy[x].add(y)
        ytox[y].add(x)
    else:
        fold = line.strip().split('=')
        folds.append((fold[0][-1],int(fold[1])))

first = True
while len(folds) > 0:
    foldAxis,foldLine = folds.pop(0)
    foldingAxisDict = xtoy if foldAxis == 'x' else ytox
    oppositeAxisDict = ytox if foldAxis == 'x' else xtoy
    for i in range(foldLine,maxX+1 if foldAxis == 'x' else maxY+1):
        for j in foldingAxisDict[i]:
            oppositeAxisDict[j].remove(i)
            oppositeAxisDict[j].add(foldLine - (i - foldLine))
            foldingAxisDict[(foldLine - (i - foldLine))].add(j)
        del foldingAxisDict[i]
    if foldAxis == 'x':
        maxX = foldLine-1
    else:
        maxY = foldLine-1
    if first:
        count = 0
        for x in range(maxX+1):
            count += len(xtoy[x])
        print("Part 1:",count)
        first = False

print("Part 2:")
grid = [['.' for x in range(maxX+1)] for y in range(maxY+1)]
for x in range(maxX+1):
    for y in xtoy[x]:
        grid[y][x] = '#'
for line in grid:
    print(''.join(line))

####.####.#....####...##..##..###..####.
#....#....#....#.......#.#..#.#..#.#....
###..###..#....###.....#.#....#..#.###..
#....#....#....#.......#.#.##.###..#....
#....#....#....#....#..#.#..#.#.#..#....
####.#....####.#.....##...###.#..#.#....