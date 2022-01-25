from collections import deque

def run_hash(nums, lengths, index, skip):
    for l in lengths:
        for i in range(l//2):
            temp = nums[(index+i)%len(nums)]
            nums[(index+i)%len(nums)] = nums[(index+l-1-i)%len(nums)]
            nums[(index+l-1-i)%len(nums)] = temp
        index = (index + l + skip) % len(nums)
        skip += 1
    return nums,index,skip

def knot_hash(string):
    nums = [i for i in range(256)]
    lengths = [ord(c) for c in string]
    lengths.extend([17,31,73,47,23])
    index = skip = 0
    for j in range(64):
        nums,index,skip = run_hash(nums, lengths, index, skip)
    dense_hash = []
    for i in range(16):
        result = nums[16*i]
        for j in range(1,16):
            result = result ^ nums[16*i + j]
        dense_hash.append(result)
    hexes = [hex(n)[2:] for n in dense_hash]
    for i in range(len(hexes)):
        if len(hexes[i]) < 2:
            hexes[i] = "0"+hexes[i]
    return "".join(hexes)
    
on = set()
for row in range(128):
    h = knot_hash("xlqgujun-"+str(row))
    b = str(bin(int(h,16))[2:].zfill(128))
    for i in range(128):
        if b[i] == "1":
            on.add((i,row))
print("Part 1:",len(on))

groups = 0
visited = set()
stack = deque()
adjacency = [(1,0),(-1,0),(0,1),(0,-1)]
for x in range(128):
    for y in range(128):
        if (x,y) in on and (x,y) not in visited:
            groups += 1
            stack.append( (x,y) )
            while stack:
                a,b = stack.popleft()
                visited.add((a,b))
                for i,j in adjacency:
                    if (a+i,b+j) in on and (a+i,b+j) not in visited:
                        stack.append( (a+i,b+j) )
print("Part 2:",groups)