from collections import deque

pieces = [(int(d.split("/")[0]),int(d.split("/")[1])) for d in open("Resources/input24.txt").readlines()]
stack = deque()
# (current pin-count to connect, total weight, length, visited set)
stack.append( (0, 0, 0, set()) )
max_weight = max_length = max_length_weight = 0
while stack:
    pins,weight,length,visited = stack.popleft()
    last_piece = True
    for a,b in pieces:
        if (a,b) not in visited and pins in (a,b):
            last_piece = False
            new_visited = visited.copy()
            new_visited.add( (a,b) )
            stack.append( ((a if pins == b else b), weight+a+b, length+1, new_visited) )
    if last_piece:
        max_weight = max(max_weight,weight)
        if length > max_length:
            max_length = length
            max_length_weight = weight
        elif length == max_length:
            max_length_weight = max(max_length_weight,weight)    
print("Part 1:",max_weight,"\nPart 2:",max_length_weight)