import networkx

def part1():
    g = networkx.Graph()
    for line in open("input.txt"):
        inp,out_raw = line.split(": ")
        for out in out_raw.split():
            g.add_edge(inp, out, capacity=1)
    
    for s in g.nodes():
        for d in g.nodes():
            if s == d:
                continue
            cut_value, (left,right) = networkx.minimum_cut(g, s, d)
            if cut_value == 3:
                return len(left)*len(right)

if __name__ == "__main__":
    print("Part 1:",part1())