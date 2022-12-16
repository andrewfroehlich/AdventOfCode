import re
from collections import deque

# Find steps required to get from source to target valve
def min_path(source,target,raw_paths,paths):
    if target in paths:
        return paths[target][source]
    bfs = deque([(source,0)])
    visited = set([source])
    while bfs:
        current,steps = bfs.popleft()
        if current == target:
            return steps
        for next_hop in raw_paths[current]:
            if next_hop not in visited:
                visited.add(next_hop)
                bfs.append( (next_hop,steps+1) )
    return -1
  
def parse_input(file):
    # Parse raw data
    flows,raw_paths,paths = dict(),dict(),dict()
    for line in open(file).read().splitlines():
        flow_rate = int(re.findall(r"\-?\d+", line)[0])
        line_split = line.split()
        this_valve = line_split[1]
        target_valves = []
        for i in range(9,len(line_split)):
            target_valves.append(line_split[i][0:2])
        if flow_rate > 0 or this_valve == "AA":
            flows[this_valve] = flow_rate
        raw_paths[this_valve] = target_valves
    
    # Determine steps required to move between any two valves with a flow rate
    for src in flows:
        paths[src] = dict()
        for target in flows:
            if src != target:
                paths[src][target] = min_path(src,target,raw_paths,paths)
    
    return flows,paths

def part1(flows,paths):
    bfs = deque([("AA",0,0,set(["AA"]))]) #current valve, step count, pressure relieved,visited
    max_pressure = 0
    while bfs:
        current,step,pressure,visited = bfs.popleft()
        if flows[current] > 0 and step <= 28:
            step += 1
            pressure += (30-step) * flows[current]
        path_continued = False
        for target in paths[current]:
            if target not in visited and step+paths[current][target] <= 28:
                path_continued = True
                new_visited = visited.copy()
                new_visited.add(target)
                bfs.append( (target, step+paths[current][target], pressure, new_visited) )
        if not path_continued and step <= 30:
            max_pressure = max(max_pressure, pressure)
    return max_pressure

def part2(flows,paths):
    #my valve, my step, elephant valve, elephant step, pressure relieved, visited, el_moving (count elephants valve)
    bfs = deque([("AA",0,"AA",0,0,set(["AA"]),True)]) 
    max_pressure = 0
    while bfs:
        current,step,el_cur,el_step,pressure,visited,el_moving = bfs.pop() # dfs for short-circuiting
        
        #add pressures of current valve. only add elephant pressure if elephant is still moving
        if flows[current] > 0 and step <= 24:
            step += 1
            pressure += (26-step) * flows[current]
        if flows[el_cur] > 0 and el_step <= 24 and el_moving:
            el_step += 1
            pressure += (26-el_step) * flows[el_cur]
            
        #short-circuit if this path can't be best
        max_possible,min_step = 0,min(step,el_step)
        for valve in flows:
            if valve not in visited:
                max_possible += (26-1-step) * flows[valve]
        if pressure+max_possible < max_pressure:
            continue
        
        #find all possible paths from here
        for target in paths[current]:
            if target not in visited and step+paths[current][target] <= 24:
                new_visited = visited.copy()
                new_visited.add(target)
                for el_target in paths[el_cur]:
                    if el_target not in new_visited and el_step+paths[el_cur][el_target] <= 24:
                        el_visited = new_visited.copy()
                        el_visited.add(el_target)
                        bfs.append( (target, step+paths[current][target], el_target, el_step+paths[el_cur][el_target], pressure, el_visited, True) )
                if step+paths[current][target] <= 24 and el_step <= 24:
                    bfs.append( (target, step+paths[current][target], el_cur, el_step, pressure, new_visited, False) )
        
        #whether we have stopped moving or not, check if we have reached the highest pressure relief
        if step <= 26 and el_step <= 26:
            max_pressure = max(max_pressure, pressure)
    return max_pressure

flows,paths = parse_input("input16.txt")
print("Part 1:",part1(flows,paths))
print("Part 2:",part2(flows,paths))