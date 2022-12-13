from functools import cmp_to_key

# -1 is in-order, 1 is out of order, 0 is continue
def compare(left,right):
    if isinstance(left,int) and isinstance(right,int):
        return -1 if left < right else (1 if left > right else 0)
    elif isinstance(left,int) and isinstance(right,list):
        left = [left]
    elif isinstance(left,list) and isinstance(right,int):
        right = [right]
    for i in range(len(left)):
        if i >= len(right):
            return 1
        c = compare(left[i],right[i])
        if c != 0:
            return c
    if len(right) > len(left):
        return -1
    return 0

lines = open("input13.txt").read().splitlines()
lines2 = [ [[2]] , [[6]] ]
part1 = 0
for i in range(0, len(lines), 3):
    left = eval(lines[i])
    lines2.append(left)
    right = eval(lines[i+1])
    lines2.append(right)
    if compare(left,right) == -1:
        part1 += (i//3 + 1)
print("Part 1:",part1)

slist = sorted(lines2, key=cmp_to_key(compare))
print("Part 2:",(slist.index([[2]])+1)*(slist.index([[6]])+1))