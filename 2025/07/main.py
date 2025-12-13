from collections import defaultdict

def parse():
    beams,tachyon = defaultdict(int),set()
    for y,line in enumerate(open("input.txt")):
        for x,char in enumerate(line.strip()):
            if char == "^":
                tachyon.add((x,y))
            elif char == "S":
                beams[(x,y)] = 1
    return beams,tachyon,y

def solve(beams,tachyon,max_y,part2=False):
    next_beams,current_y,splits = defaultdict(int),0,0
    while beams and current_y <= max_y:
        for (x,y),count in beams.items():
            if (x,y+1) in tachyon:
                next_beams[(x-1,y+1)] += count
                next_beams[(x+1,y+1)] += count
                splits += 1
            else:
                next_beams[(x,y+1)] += count
        beams,next_beams = next_beams,defaultdict(int)
        current_y += 1
    return splits if not part2 else sum(beams.values())

if __name__ == "__main__":
    beams,tachyon,max_y = parse()
    print("Part 1:",solve(beams.copy(),tachyon,max_y))
    print("Part 2:",solve(beams.copy(),tachyon,max_y,True))