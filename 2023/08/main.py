from math import lcm # requires python 3.9

def parse():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    directions = lines[0]
    m = {}
    for i in range(2,len(lines)):
        m[lines[i][0:3]] = (lines[i][7:10],lines[i][12:15])
    return directions,m

def part1():
    directions,m = parse()
    current = 'AAA'
    step = 1
    while current != 'ZZZ':
        current = m[current][0] if directions[(step-1) % len(directions)] == 'L' else m[current][1]
        step += 1
    return step-1
    
def part2():
    directions,m = parse()
    currents = []
    for k in m.keys():
        if k[-1] == 'A':
            currents.append(k)
    steps = []
    for i in range(len(currents)):
        step = 1
        while currents[i][-1] != 'Z':
            currents[i] = m[currents[i]][0] if directions[(step-1) % len(directions)] == 'L' else m[currents[i]][1]
            step += 1
        steps.append(step-1)
    return lcm(*steps)

if __name__ == '__main__':
    print("Part 1:",part1())
    print("Part 2:",part2())