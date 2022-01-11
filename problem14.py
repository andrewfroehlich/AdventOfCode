from collections import defaultdict

def run(steps):
    t,pairs = open("input14.txt").read().split("\n\n")
    polymers = dict((i for i in l.split(" -> ")) for l in pairs.strip().split('\n'))
    paircount = defaultdict(int)

    #convert input to pairs 
    for index in range(len(t)-1):
        paircount[t[index]+t[index+1]] += 1

    #run steps
    for s in range(steps):
        newpaircount = defaultdict(int)
        for key in paircount:
            newpaircount[key[0]+polymers[key]] += paircount[key]
            newpaircount[polymers[key]+key[1]] += paircount[key]
        paircount = newpaircount

    #enumerate all possible chars
    allchars = set()
    for key in polymers:
        allchars.add(key[0])
        allchars.add(key[1])
        allchars.add(polymers[key])

    #find min/max of all chars
    maxCount = minCount = -1
    for c in allchars:
        count = 0
        for key in paircount:
            if c == key[0]:
                count += paircount[key]
        count += 1 if t[-1] == c else 0
        maxCount = count if count > maxCount else maxCount
        minCount = count if (count < minCount or minCount == -1) else minCount
    return maxCount-minCount
    
print("Part 1:",run(10))
print("Part 2:",run(40))