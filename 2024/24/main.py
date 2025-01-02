from collections import deque

def process_input():
    raw_vals,raw_connects = open("input.txt").read().split("\n\n")
    wires,connections = dict(),deque()
    for line in raw_vals.split("\n"):
        w,val = line.split(": ")
        wires[w] = (val == "1")
    for line in raw_connects.split("\n"):
        w1,op,w2,_,w3 = line.split(" ")
        connections.append( (w1,w2,w3,op) )
    return wires,connections

def part1():
    wires,connections = process_input()
    while connections:
        w1,w2,w3,op = connections.popleft()
        if w1 in wires and w2 in wires:
            match op:
                case "AND":
                    wires[w3] = wires[w1] and wires[w2]
                case "OR":
                    wires[w3] = wires[w1] or wires[w2]
                case "XOR":
                    wires[w3] = wires[w1] ^ wires[w2]
        else:
            connections.append( (w1,w2,w3,op) )
    z_wires = sorted([key for key in wires if key.startswith('z')])
    return sum(2**i for i, wire in enumerate(z_wires) if wires[wire])

if __name__ == "__main__":
    print("Part 1:",part1())