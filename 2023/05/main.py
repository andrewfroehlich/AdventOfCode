def parseFile():
    with open('input.txt', 'r') as f:
        sections = f.read().split("\n\n")
    seeds = [int(s) for s in sections[0].split(": ")[-1].split()]
    sections.pop(0)
    return seeds,sections

def part1():
    values,sections = parseFile()
    for section in sections:
        lines = section.splitlines()
        ranges = [tuple(int(d) for d in l.split()) for l in lines[1:]]
        
        values_new = []
        for v in values:
            found = -1
            for dest_start,src_start,length in ranges:
                if src_start <= v < src_start + length:
                    found = dest_start + (v - src_start)
                    break #go to next value
            if found == -1:
                found = v #if not found in the mapping, keep the same value
            values_new.append(found)
        values = values_new
    return min(values)

def part2():
    seed_list,sections = parseFile()
    seeds = [(seed_list[i],seed_list[i+1]) for i in range(0,len(seed_list),2)]
    
    mappings = []
    for section in sections:
        lines = section.splitlines()
        ranges = [tuple(int(d) for d in l.split()) for l in lines[1:]]
        mappings.append(ranges)
    
    location = 0 #starting at location 0, brute force until we find a valid seed
    while True:
        current = location
        for map_i in range(len(mappings)-1, -1, -1):
            found = -1
            for dest_start,src_start,length in mappings[map_i]:
                if dest_start <= current < dest_start + length:
                    found = src_start + (current - dest_start)
                    break #go to next value
            if found == -1:
                found = current #if not found in the mapping, keep the same value
            current = found
        
        for start,rnge in seeds:
            if start <= current < start+rnge:
                return location
        location += 1

if __name__ == '__main__':
    print("Part 1:",part1())
    print("Part 2:",part2())