inp = 3400000
house = 700000

found1 = found2 = False
while True:
    current = 0
    part2 = 0
    for i in range(1,1001):
        if house % i == 0:
            current += i
            current += house / i
            if 50*i >= house:
                part2 += 11*i
            if 50*(house/i) >= house:
                part2 += 11*(house/i)
    for i in range(1,house//1000):
        if house % i == 0:
            current += i
            if 50*i >= house:
                part2 += 11*i
    if not found1 and current >= inp:
        print("Part 1:", house)
        found1 = True
    if nout found2 and part2 >= inp*10:
        print("Part 2:", house)
        found2 = True
    if found1 and found2:
        break
    house += 1