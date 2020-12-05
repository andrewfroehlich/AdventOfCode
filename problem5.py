
def problem5():
    f = open("/home/ec2-user/environment/AOC/Resources/problem5.txt")
    maxVal = 0
    ids = set()
    for current in f.readlines():
        row = int(current[:7].replace("F","0").replace("B","1"),2)
        seat = int(current[7:].replace("L","0").replace("R","1"),2)
        seatId = row*8 + seat
        ids.add(seatId)
        maxVal = max(maxVal, seatId)
    
    print(maxVal)
    currentId = maxVal
    while True:
        if currentId in ids:
            currentId -= 1
        else:
            return currentId
    return 0

print(problem5())