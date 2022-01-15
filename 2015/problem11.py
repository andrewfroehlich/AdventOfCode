def incrementChar(c):
    if c == 'z':
        return 'a',True
    else:
        return chr(ord(c)+1),False

p = list("cqjxjnds")
currentPart = 1
while True:
    #perform one increment
    carry = False
    for i in range(len(p)-1, -1, -1):
        newchar,carry = incrementChar(p[i])
        p[i] = newchar
        if not carry:
            if newchar in ('i','o','l'):
                p[i],carry = incrementChar(newchar)
                for i in range(i+1,len(p)):
                    p[i] = 'a'
            break
    if carry:
        p.insert(0, 'a')
    
    #check other rules
    p2 = p1 = None
    threeStraight = False
    doubleLetters = 0
    lastDoubleIndex = -1
    for i in range(len(p)):
        c = p[i]
        if p1 and p1 == c and lastDoubleIndex != i-1:
            lastDoubleIndex = i
            doubleLetters += 1
        elif p2 and p1 and p1 == chr(ord(p2)+1) and c == chr(ord(p1)+1):
            threeStraight = True
        p2 = p1
        p1 = c
    if threeStraight and doubleLetters >= 2:
        print("Part {}: {}".format(currentPart,"".join(p)))
        currentPart += 1
        if currentPart > 2:
            break