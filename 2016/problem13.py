from collections import deque

def isValid(x,y):
    val = (x*x) + (3*x) + (2*x*y) + y + (y*y) + 1358
    setBits = [ones for ones in bin(val)[2:] if ones=='1']
    return len(setBits) % 2 == 0

def runDFS(part2):
    stack = deque()
    stack.append((1,1,0))
    visited = dict()
    adjacency = [(-1,0),(1,0),(0,-1),(0,1)]
    while stack:
        c_x,c_y,steps = stack.popleft()
        visited[(c_x,c_y)] = steps
        if not part2 and (c_x,c_y) == (31,39):
            return steps
        if steps < 50 or not part2:
            for a_x,a_y in adjacency:
                x,y = c_x+a_x,c_y+a_y
                if (x,y) not in visited and x >= 0 and y >= 0 and isValid(x,y):
                    stack.append( (x,y,steps+1) )
    return len(visited)
        
print("Part 1:",runDFS(False),"\nPart 2:",runDFS(True))