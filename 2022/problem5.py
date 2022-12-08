from collections import deque

def execute(part2):
    lines = open("input5.txt").readlines()
    break_index = 0
    while lines[break_index].strip() != "":
        break_index += 1
    stacks = [deque() for _ in range(9)]
    for i in range(break_index-2,-1,-1):
        for c in range(9):
            if 'A' <= lines[i][(c*4)+1] <= 'Z':
                stacks[c].append(lines[i][(c*4)+1])
    for i in range(break_index+1,len(lines)):
        _,count,_,source,_,dest = lines[i].split()
        if not part2:
            for j in range(int(count)):
                stacks[int(dest)-1].append(stacks[int(source)-1].pop())
        else:
            buffer = []
            for j in range(int(count)):
                buffer.append(stacks[int(source)-1].pop())
            for j in range(int(count)):
                stacks[int(dest)-1].append(buffer.pop())
    return "".join([s.pop() for s in stacks])

print("Part 1:",execute(False))
print("Part 1:",execute(True))