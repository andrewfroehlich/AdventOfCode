buckets = [int(d) for d in open("Resources/input6.txt").readline().split()]
visited = dict()
steps = 0 #redistributions completed
while tuple(buckets) not in visited:
    visited[tuple(buckets)] = steps
    max_value = max(buckets)
    max_index = buckets.index(max_value)
    buckets[max_index] = 0
    for i in range(max_value):
        index = (max_index+1+i)%len(buckets)
        buckets[index] += 1
    steps += 1
print("Part 1:", steps,"\nPart 2:", steps-visited[tuple(buckets)])