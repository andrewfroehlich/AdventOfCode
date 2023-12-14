import re

def parseFile():
    lines = open("input.txt").read().splitlines()
    cubes,rocks = set(),set()
    for y in range(-1,len(lines)+1):
        for x in range(-1,len(lines[0])+1):
            if y in (-1,len(lines)) or x in (-1,len(lines[0])) or lines[y][x] == "#":
                cubes.add( (x,y) )
            elif lines[y][x] == "O":
                rocks.add( (x,y) )
    return cubes,rocks,len(lines)

def part1():
    cubes,rocks,max_y = parseFile()
    rocks = tilt(cubes,rocks,(0,-1))
    return sum([max_y - y for x,y in rocks])

def tilt(cubes,rocks,direction):
    moved = True
    i,j = direction
    while moved:
        moved = False
        new_rocks = set()
        while rocks:
            x,y = rocks.pop()
            if (x+i,y+j) not in cubes and (x+i,y+j) not in new_rocks and (x+i,y+j) not in rocks:
                new_rocks.add( (x+i,y+j) )
                moved = True
            else:
                new_rocks.add( (x,y) )
        rocks = new_rocks
    return rocks

def part2():
    # run enough cycles to settle into a pattern, saving total load values per cycle
    cubes,rocks,max_y = parseFile()
    loads = []
    for cycle in range(1,2*max_y+1):
        for direction in [(0,-1),(-1,0),(0,1),(1,0)]:
            rocks = tilt(cubes,rocks,direction)
        loads.append(str(sum([max_y - y for x,y in rocks])))

    # find the shortest repeating sequence in the load values, assuming one exists
    regex = re.compile(r'(.+ .+)( \1)+')
    sequence = loads
    while match := regex.search(" ".join(sequence)):
        sequence = match.group(1).split()
    
    # find the last index of sequence within loads, and extrapolate out to expected cycle count
    for i in range(len(loads)-len(sequence)-1,len(sequence),-1):
        if loads[i:i+len(sequence)] == sequence:
            return sequence[ (1000000000-1-i) % len(sequence) ]

if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())