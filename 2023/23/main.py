from collections import deque, defaultdict

def parse_to_graph():
    lines = open("input.txt").read().splitlines()
    adjacency = [(0,-1),(-1,0),(0,1),(1,0)]
    
    nodes = { 'A':(1,0), 'END':(len(lines[0])-2,len(lines)-1) } # node to coordinate
    node_index = { (1,0):'A', (len(lines[0])-2,len(lines)-1):'END' } # coordinate to node
    last_created_node = 'A'
    bfs = deque( [((1,0),(0,0),'A',0)] )
    directed_node_lengths,reverse_lengths = defaultdict(list),defaultdict(list)

    while bfs:
        current,last_step,from_node,steps = bfs.popleft()
        if current in node_index and node_index[current] == 'END':
            directed_node_lengths[from_node].append( ('END',steps) )
            continue
        
        # we're on a node if we have no adjacent .s (all slopes and forest)
        x,y = current
        if sum([1 if lines[y+j][x+i] == '.' else 0 for i,j in adjacency]) == 0:
            next_node = node_index[current] if current in node_index else None
            if next_node: # if the node already exists, we don't need to create a new node and do that processing
                directed_node_lengths[from_node].append( (next_node,steps) )
                reverse_lengths[next_node].append( (from_node,steps) )
                continue
            last_created_node = chr(ord(last_created_node)+1)
            next_node = last_created_node
            directed_node_lengths[from_node].append( (next_node,steps) )
            reverse_lengths[next_node].append( (from_node,steps) )
            nodes[last_created_node] = current
            node_index[current] = last_created_node
            from_node,steps = next_node,0 # reset the from_node and steps for the below loop
        
        for i,j in adjacency: 
            dx,dy = x+i,y+j
            if lines[dy][dx] != '#' and (lines[y][x] == '.' or adjacency["^<v>".index(lines[y][x])] == (i,j)) and \
             last_step != (-i,-j) and (lines[dy][dx] == '.' or adjacency["^<v>".index(lines[dy][dx])] != (-i,-j)):
                bfs.append( ((dx,dy), (i,j), from_node, steps+1) )
    return nodes,directed_node_lengths,reverse_lengths

def solve(part=1):
    nodes,lengths,rev_lengths = parse_to_graph()
    bfs = deque( [('A',0,'A')] ) # current node, steps taken, full path
    ans = 0
    while bfs:
        node,steps,path = bfs.popleft()
        if node == 'END':
            ans = max(ans, steps)
            continue
        for next_node,steps_to in (lengths[node]+rev_lengths[node] if part==2 else lengths[node]):
            if next_node not in path: 
                bfs.append( (next_node,steps+steps_to,path+next_node) )
    return ans
    
if __name__ == "__main__":
    print("Part 1:", solve())
    print("Part 2:", solve(2))