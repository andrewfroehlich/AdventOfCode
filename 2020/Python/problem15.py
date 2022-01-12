def run(turns):
    inp = [int(j) for j in open("../Resources/problem15.txt").readline().split(",")]
    turn = 1
    turnsSince = 0
    d = dict()
    for i in inp:
        turnsSince = turn - d[i] if (i in d) else 0
        d[i] = turn
        turn += 1
    for turn in range(turn,turns+1):
        val = turnsSince
        turnsSince = turn - d[val] if (val in d) else 0
        d[val] = turn
    return val

print("Part 1:",run(2020))
print("Part 1:",run(30000000))