from collections import deque
import math

hexQueue = deque([l for l in open("input16.txt").read().strip()])
bitQueue = deque()
hexToB = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
operations = deque()
part1 = part2 = 0

class Operation:
    def __init__(self,isPackets,count,operator):
        self.isPackets = isPackets
        self.count = count
        self.operator = operator
        self.literals = []
    def __str__(self):
        return "Op={}, Count={}, isPackets={}, LiteralCount={}".format(self.operator,self.count,self.isPackets,len(self.literals))
    def execute(self):
        if self.operator == 0:
            return sum(self.literals)
        elif self.operator == 1:
            return math.prod(self.literals)
        elif self.operator == 2:
            return min(self.literals)
        elif self.operator == 3:
            return max(self.literals)
        elif self.operator == 5:
            return 1 if self.literals[0] > self.literals[1] else 0
        elif self.operator == 6:
            return 1 if self.literals[0] < self.literals[1] else 0
        elif self.operator == 7:
            return 1 if self.literals[0] == self.literals[1] else 0

def addBits():
    global hexQueue,bitQueue
    if hexQueue:
        nextBits = hexToB[hexQueue.popleft()]
        for b in nextBits:
            bitQueue.append(b)

def getBits(count):
    global hexQueue,bitQueue,operations
    while len(bitQueue) < count and hexQueue:
        addBits()
    bits = ""
    for i in range(count):
        if bitQueue:
            bits = bits + bitQueue.popleft()
    for rem in operations:
        if not rem.isPackets:
            rem.count -= len(bits)
    return bits


while len(hexQueue)>2:
    if operations and operations[0].isPackets:
        operations[0].count -= 1
    p_version = int(getBits(3),2)
    part1 += p_version
    p_type = int(getBits(3),2)
    if p_type == 4: #literal value
        p_value_binary = ""
        while True:
            leadbit = getBits(1)
            p_value_binary += getBits(4)
            if leadbit == '0':
                break
        part2 = int(p_value_binary,2)
        if operations:
            operations[0].literals.append(part2)
    else: #operator packet
        length_type_id = getBits(1)
        if length_type_id == '1': #packets
            operations.appendleft(Operation(True,int(getBits(11),2),p_type))
        else: #bits
            operations.appendleft(Operation(False,int(getBits(15),2),p_type))
    
    while len(operations) > 0 and operations[0].count == 0: #execute ready operations
        part2 = operations.popleft().execute()
        if operations:
            operations[0].literals.append(part2)
    
    if len(operations) == 0:
        bitQueue.clear()

print("Part 1:",part1)
print("Part 2:",part2)