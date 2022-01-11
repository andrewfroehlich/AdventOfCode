
def problem5():
    f = open("/home/ec2-user/environment/AOC/Resources/problem5.txt")
    maxVal = 0
    ids = set()
    for current in f.readlines():
        seatId = int(current.replace("F","0").replace("B","1")
            .replace("L","0").replace("R","1"),2)
        ids.add(seatId)
        maxVal = max(maxVal, seatId)
    
    print(maxVal)
    currentId = maxVal
    while currentId in ids:
        currentId -= 1
    return currentId

print(problem5())