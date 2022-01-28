from collections import defaultdict
import math

def getValue(var, reg):
    return int(var) if var.strip("-").isnumeric() else reg[var]
    
def part1():
    lines = open("Resources/input23.txt").readlines()
    reg = defaultdict(int)
    index = part1 = 0
    while index >= 0 and index < len(lines):
        ins,x,y = lines[index].strip().split()
        if ins == "set":
            reg[x] = getValue(y,reg)
        elif ins == "sub":
            reg[x] = reg[x] - getValue(y,reg)
        elif ins == "mul":
            reg[x] = reg[x] * getValue(y,reg)
            part1 += 1
        else: #jnz
            if getValue(x,reg) != 0:
                index += getValue(y,reg)
            else:
                index += 1
        
        if ins != "jnz":
            index += 1
    return part1

print("Part 1:",part1())

def isPrime(x):
    for mult in range(2,int(math.sqrt(x)+1)):
        if x % mult == 0:
            return False
    return True

#If a=1, this is effectively the code that is run:
b = 105700
h = 0
while b <= 122700:
    h += 0 if isPrime(b) else 1
    b += 17
print("Part 2:",h)