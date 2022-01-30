from collections import defaultdict
import bisect

def prepare():
    prereqs,reverse = defaultdict(set),defaultdict(set)
    origin = set()
    for line in open("Resources/input7.txt"):
        _,prestep,*_,step,_,_ = line.split()
        prereqs[step].add(prestep)
        reverse[prestep].add(step)
        origin.discard(step)
        if prestep not in prereqs:
            origin.add(prestep)
    ready = list(origin)
    ready.sort()
    return ready, prereqs, reverse

ready, prereqs, reverse = prepare()
complete = []
while ready:
    current = ready.pop(0)
    complete.append(current)
    for step in reverse[current]:
        prereqs[step].discard(current)
        if len(prereqs[step]) == 0:
            bisect.insort(ready, step)
print("Part 1:","".join(complete))

ready, prereqs, reverse = prepare()
complete = []
time = -1
workers_ready = 5
worker_avail_times = []
while ready or workers_ready < 5:
    time += 1
    while worker_avail_times and worker_avail_times[0][0] == time:
        workers_ready += 1
        _,current = worker_avail_times.pop(0)
        complete.append(current)
        for step in reverse[current]:
            prereqs[step].discard(current)
            if len(prereqs[step]) == 0:
                bisect.insort(ready, step)
    if ready and workers_ready:
        for i in range(min(len(ready),workers_ready)):
            workers_ready -= 1
            current = ready.pop(0)
            bisect.insort(worker_avail_times, (time + 61 + ord(current) - ord('A'), current))
print("Part 2:", time)