import sys
import heapq

def isValid(x,y,maxX,maxY):
    return x>=0 and y>=0 and x<=maxX and y<=maxY

def dijkstra(graph):
    distance = [[sys.maxsize for _ in range(len(graph[0]))] for __ in range(len(graph))]
    distance[0][0] = 0
    visited = set()
    neighbors = [(-1,0),(0,1),(1,0),(0,-1)]
    min_heap = [(0, (0,0))] 
    while min_heap:
        cur_dist, cur_coord = heapq.heappop(min_heap)
        if cur_coord in visited:
            continue
        visited.add(cur_coord)

        x,y = cur_coord
        for i,j in neighbors:
            if isValid(x+i,y+j,len(graph)-1,len(graph[0])-1) and (x+i,y+j) not in visited:
                this_dist = cur_dist + graph[x+i][y+j]
                if this_dist < distance[x+i][y+j]:
                    distance[x+i][y+j] = this_dist
                    if distance[-1][-1] != sys.maxsize:
                        return distance[-1][-1]
                    heapq.heappush(min_heap, (this_dist, (x+i,y+j)))
    return -1

def build_mega_graph(base_graph):
    graph = [[0 for c in range(len(base_graph[0])*5)] for l in range(len(base_graph)*5)]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            incrementer = i//len(base_graph) + j//len(base_graph[0])
            val = base_graph[i % len(base_graph)][j % len(base_graph[0])] + incrementer
            while val > 9:
                val -= 9
            graph[i][j] = val
    return graph

graph = [[int(c) for c in l] for l in open("input15.txt").read().strip().split('\n')]
print("Part 1:",dijkstra(graph))
print("Part 2:",dijkstra(build_mega_graph(graph)))