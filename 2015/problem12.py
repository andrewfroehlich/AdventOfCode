import re
import json
from collections import deque 

inp = open("Resources/input12.txt").readline()
print("Part 1:",sum([int(s) for s in re.findall("[-\d]+", inp)]))

data = json.loads(inp)
total = 0
toTraverse = deque(data)
while len(toTraverse)>0:
    obj = toTraverse.popleft()
    if type(obj) is list:
        for i in obj:
            if type(i) is int:
                total += i
            elif type(i) in (list,dict):
                toTraverse.append(i)
    elif type(obj) is dict:
        addToTraverse = []
        addToTotal = 0
        foundRed = False
        for k in obj:
            if obj[k] == "red":
                foundRed = True
                break
            elif type(obj[k]) is int:
                addToTotal += obj[k]
            elif type(obj[k]) in (dict,list):
                addToTraverse.append(obj[k])
        if not foundRed:
            total += addToTotal
            for o in addToTraverse:
                toTraverse.append(o)
print("Part 2:",total)