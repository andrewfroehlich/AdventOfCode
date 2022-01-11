from collections import deque

def part1():
    q = deque()
    s = set()
    f = open("../Resources/problem9.txt")
    for line in f:
        value = int(line)
        if len(q) < 25:
            q.append(value)
            s.add(value)
            continue
        valid = False
        for v in q:
            if (value - v) in s:
                valid = True
                break
        if not valid:
            return value
        s.remove(q.popleft())
        q.append(value)
        s.add(value)

def part2(target):
    q = deque()
    range_sum = 0
    f = open("../Resources/problem9.txt")
    for line in f:
        q.append(int(line))
        range_sum += int(line)
        while range_sum > target:
            removed = q.popleft()
            range_sum -= removed
        if range_sum == target:
            return min(q) + max(q)

target = part1()
print("Part 1:",target)
print("Part 2:",part2(target))