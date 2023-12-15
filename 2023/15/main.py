from collections import defaultdict

def hash(s):
    h = 0
    for c in s:
        h = ((h + ord(c)) * 17) % 256
    return h

def part1(values):
    return sum([hash(s) for s in values])

def part2(values):
    hm = defaultdict(list)
    for s in values:
        if s[-1] == "-":
            label = s[:-1]
            bucket = hash(label)
            hm[bucket] = [(l,f) for l,f in hm[bucket] if l != label]
        else:
            label,focal = s.split("=")
            bucket = hash(label)
            matching = [i for i in range(len(hm[bucket])) if hm[bucket][i][0] == label]
            if matching:
                hm[bucket][matching[0]] = (label,int(focal))
            else:
                hm[bucket].append( (label,int(focal)) )
    return sum([sum([(k+1)*(i+1)*(v[i][1]) for i in range(len(v))]) for k,v in hm.items()])

if __name__ == '__main__':
    values = open("input.txt").readline().split(",")
    print("Part 1:",part1(values))
    print("Part 2:",part2(values))