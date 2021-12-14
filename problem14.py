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
    current = nextNode
    nextNode = current.next
    for c in allchars:
        countsSum[c] = countsSum[c] + cache20[key][c] - (1 if key[1] == c and nextNode is not None else 0) #remove double counting
print("Counts Sum Complete")

# Print all counts and the Part 2 answer
maxCount = minCount = -1
for c in allchars:
    print(c,countsSum[c])
    maxCount = countsSum[c] if countsSum[c] > maxCount else maxCount
    minCount = countsSum[c] if (countsSum[c] < minCount or minCount == -1) else minCount
print("Part 2:",maxCount-minCount)


#V 439051102821
#P 977393099208
#N 3067784388562
#H 3800433128803
#S 619697444903
#C 2804420769138
#K 1634200947813
#B 1382279882429
#O 3898229386832
#F 2267250700179
#Part 2: 3459178284011

#right:
F 2267248527101
K 1634199382184
C 2804418100771
O 3898225660655
B 1382278561174
N 3067781482737
P 977392169054
H 3800429511266
V 439050679634
S 619696853169
Part 2: 3459174981021