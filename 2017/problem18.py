from collections import defaultdict,deque

def getValue(var, reg):
    return int(var) if var.strip("-").isnumeric() else reg[var]

def run(lines, part1, index, reg, myQueue, otherQueue):
    last_sound = -1
    while index >= 0 and index < len(lines):
        inst = lines[index].strip()
        if inst[0:3] == "snd":
            if part1:
                last_sound = getValue(inst.split()[1],reg)
            else:
                otherQueue.append(getValue(inst.split()[1],reg))
        elif inst[0:3] == "rcv":
            if part1:
                if getValue(inst.split()[1],reg) != 0:
                    return last_sound
            else:
                if myQueue:
                    reg[inst.split()[1]] = myQueue.popleft()
                else:
                    return index,reg,myQueue,otherQueue
        elif inst[0:3] == "jgz":
            _,x,y = inst.split()
            if getValue(x, reg) > 0:
                index += getValue(y, reg)
            else:
                index += 1
        else:
            i,r,val = inst.split()
            v = getValue(val,reg)
            if i == "set":
                reg[r] = v
            elif i == "add":
                reg[r] += v
            elif i == "mul":
                reg[r] = reg[r] * v
            elif i == "mod":
                reg[r] = reg[r] % v
       
        if inst[0:3] != "jgz":
            index += 1
    return index,reg,myQueue,otherQueue

lines = open("Resources/input18.txt").readlines()
print("Part 1:", run(lines,True,0,defaultdict(int),None,None))

index0 = index1 = 0
queue0 = deque()
queue1 = deque()
reg0 = defaultdict(int)
reg1 = defaultdict(int)
reg1['p'] = 1
part2 = 0
while True:
    index0,reg0,queue0,queue1 = run(lines,False,index0,reg0,queue0,queue1)
    
    part2 -= len(queue0)
    index1,reg1,queue1,queue0 = run(lines,False,index1,reg1,queue1,queue0)
    part2 += len(queue0)
    
    if ((index0 < 0 or index0 >= len(lines) or len(queue0) == 0) and 
        (index1 < 0 or index1 >= len(lines) or len(queue1) == 0)):
        break
print("Part 2:",part2)