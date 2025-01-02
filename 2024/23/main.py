from collections import defaultdict
from collections import deque

def process_input(is_part2):
    paths = defaultdict(set)
    starts,bfs = set(),deque()
    for line in open("input.txt"):
        one,two = line.strip().split("-")
        paths[one].add(two)
        paths[two].add(one)
        if one[0] == 't' or is_part2:
            starts.add(one)
        if two[0] == 't' or is_part2:
            starts.add(two)
    for c in starts:
        for destination in paths[c]:
            bfs.append( (destination,(c,destination)) ) # current, (all in group)
    return paths,bfs

def can_add_to_group(new_node, current_group, paths):
    for c in current_group:
        if c not in paths[new_node]:
            return False
    return True

def part1():
    paths,bfs = process_input(False)
    three_groups = set()
    while bfs:
        current,current_group = bfs.popleft()
        for destination in paths[current]:
            if destination not in current_group and can_add_to_group(destination, current_group, paths):
                three_groups.add(tuple(sorted(list(current_group) + [destination])))
    return len(three_groups)

def part2():
    paths,bfs = process_input(True)
    visited,largest_group = set(),tuple('dummy')
    while bfs:
        current,current_group = bfs.popleft()
        largest_group = current_group if (len(current_group) > len(largest_group)) else largest_group
        for destination in paths[current]:
            if destination in current_group:
                continue
            new_group = tuple(sorted(list(current_group) + [destination]))
            if new_group not in visited and can_add_to_group(destination, current_group, paths):
                visited.add(new_group)
                bfs.append( (destination, new_group) )
    return ",".join(sorted(list(largest_group)))

if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())