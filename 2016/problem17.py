from collections import deque
import hashlib

salt = "rrrbmfta"
stack = deque()
stack.append( (1,1,"") )
open_chars = ('b','c','d','e','f')
longest_path_len = -1

while len(stack)>0:
    x,y,path = stack.popleft()
    if (x,y) == (4,4):
        if longest_path_len == -1:
            print("Part 1:",path)
        longest_path_len = max(longest_path_len, len(path))
    else:
        md5 = hashlib.md5((salt+path).encode("utf-8")).hexdigest()
        if y > 1 and md5[0:1] in open_chars:
            stack.append( (x, y-1, path+"U") )
        if y < 4 and md5[1:2] in open_chars:
            stack.append( (x, y+1, path+"D") )
        if x > 1 and md5[2:3] in open_chars:
            stack.append( (x-1, y, path+"L") )
        if x < 4 and md5[3:4] in open_chars:
            stack.append( (x+1, y, path+"R") )
print("Part 2:",longest_path_len)