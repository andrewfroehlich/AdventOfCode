f = open("input13.txt")
points = set()
folds = []
parseFolds = False
for line in f:
    if line.strip() == "":
        parseFolds = True
    elif not parseFolds:
        coord = line.strip().split(',')
        points.add((int(coord[0]),int(coord[1])))
    else:
        fold = line.strip().split('=')
        folds.append((fold[0][-1],int(fold[1])))

first = True
maxX = maxY = 0
while len(folds) > 0:
    foldAxis,foldLine = folds.pop(0)
    newset = set()
    for x,y in points:
        if foldAxis == 'x':
            newset.add((x,y) if x<foldLine else ((foldLine-(x-foldLine)),y))
        else:
            newset.add((x,y) if y<foldLine else (x,(foldLine-(y-foldLine))))
    if foldAxis == 'x':
        maxX = foldLine-1
    else:
        maxY = foldLine-1
    points = newset
    if first:
        print("Part 1:",len(points))
        first = False

print("Part 2:")
grid = [['.' for x in range(maxX+1)] for y in range(maxY+1)]
for x,y in points:
    grid[y][x] = '#'
for line in grid:
    print(''.join(line))

####.####.#....####...##..##..###..####.
#....#....#....#.......#.#..#.#..#.#....
###..###..#....###.....#.#....#..#.###..
#....#....#....#.......#.#.##.###..#....
#....#....#....#....#..#.#..#.#.#..#....
####.#....####.#.....##...###.#..#.#....