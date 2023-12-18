from heapq import heappush, heappop

def priority_dfs(m, max_consecutive, before_turn):
    adjacency = [(-1,0),(0,1),(1,0),(0,-1)]
    dfs = [(0,0,0,2,0),(0,0,0,1,0)]
    visited = set()
    while dfs:
        heat,x,y,d_index,cons = heappop(dfs)
        dx,dy = adjacency[d_index] 
        x,y = x+dx,y+dy 
        cons += 1
        if not (0 <= x < len(m[0]) and 0 <= y < len(m)) or (x,y,d_index,cons) in visited:
            continue
        heat += int(m[y][x])
        if y == len(m)-1 and x == len(m[0])-1:
            return heat
        visited.add( (x,y,d_index,cons) )
        if cons < max_consecutive:
            heappush(dfs, (heat,x,y,d_index,cons))
        if cons >= before_turn:
            heappush(dfs, (heat,x,y,(d_index+1)%4,0))
            heappush(dfs, (heat,x,y,(d_index-1)%4,0))

if __name__ == "__main__":
    m = open("input.txt").read().splitlines()
    print("Part 1:", priority_dfs(m,3,0))
    print("Part 2:", priority_dfs(m,10,4))