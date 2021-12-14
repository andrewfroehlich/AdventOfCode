import sys

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None

t,pairs = open("input14.txt").read().split("\n\n")
polymers = dict((i for i in l.split(" -> ")) for l in pairs.strip().split('\n'))
template = linkedList()
current = None
for c in t:
    if current is None:
        current = Node(c)
        template.head = current
    else:
        t = Node(c)
        current.next = t
        current = t

#build set of all possible chars
allchars = set()
for key in polymers:
    allchars.add(key[0])
    allchars.add(key[1])
    allchars.add(polymers[key])
print("Total keys",len(allchars))

#build 20-step cache of counts, e.g. for CV in 20 steps, you result in XXX C, YYY V, etc.
cache20 = dict()
for key in polymers:
    templist = linkedList()
    templist.head = Node(key[0])
    templist.head.next = Node(key[1])
    step = 0
    while step < 20:
        current = templist.head
        nextNode = current.next
        while nextNode is not None:
            insert = Node(polymers[current.data+nextNode.data])
            current.next = insert
            insert.next = nextNode
            current = nextNode
            nextNode = current.next
        step += 1
    
    counts = dict()
    current = templist.head
    while current is not None:
        if current.data in counts:
            counts[current.data] += 1
        else:
            counts[current.data] = 1
        current = current.next
    cache20[key] = counts
    print(key," cache count added")

# Run 20 steps of the original input
step = 0
while step < 20:
    current = template.head
    nextNode = current.next
    while nextNode is not None:
        insert = Node(polymers[current.data+nextNode.data])
        current.next = insert
        insert.next = nextNode
        current = nextNode
        nextNode = current.next
    step += 1
    print("Step",step,"complete")

# For each 2-char sequence in the resulting 20 step string, add the counts of running an additional 20 steps
countsSum = dict()
for c in allchars:
    countsSum[c] = 0
current = template.head
nextNode = current.next
while nextNode is not None:
    key = current.data+nextNode.data
    for c in allchars:
        countsSum[c] = countsSum[c] + cache20[key][c]
    current = nextNode
    nextNode = current.next
print("Counts Sum Complete")

# Print all counts and the Part 2 answer
maxCount = minCount = -1
for c in allchars:
    print(c,countsSum[c])
    maxCount = countsSum[c] if countsSum[c] > maxCount else maxCount
    minCount = countsSum[c] if (countsSum[c] < minCount or minCount == -1) else minCount
print("Part 2:",maxCount-minCount)