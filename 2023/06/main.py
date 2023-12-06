from operator import mul
from functools import reduce 

def parse():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    times = list(map(int, lines[0].split()[1:]))
    distances = list(map(int, lines[1].split()[1:]))
    return times,distances

def part1():
    times,distances = parse()
    options = []
    for i in range(len(times)):
        options.append(sum([1 for n in range(times[i]) if ((times[i]-n) * n > distances[i])]))
    return reduce(mul, options)

def part2():
    times,distances = parse()
    time = int("".join(map(str, times)))
    distance = int("".join(map(str, distances)))
    # find first and last viable time 
    time1 = time2 = -1
    current = 1
    while time1 == -1:
        time1 = current if (time-current)*current > distance else -1
        current += 1
    current = time-1
    while time2 == -1:
        time2 = current if (time-current)*current > distance else -1
        current -= 1
    return time2 - time1 + 1

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())