def get_char_value(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    return ord(char) - ord('A') + 27

def rucksack_value(l):
    s = set()
    for c in l[0:len(l)//2]:
        s.add(c)
    for c in l[len(l)//2:]:
        if c in s:
            return get_char_value(c)

def badge_value(l1,l2,l3):
    s1 = set()
    for c in l1.strip():
        s1.add(c)
    s2 = set()
    for c in l2.strip():
        if c in s1:
            s2.add(c)
    for c in l3.strip():
        if c in s2:
            return get_char_value(c)

lines = open("input3.txt").readlines()
part1,part2 = 0,0
for line in lines:
    part1 += rucksack_value(line.strip())
for i in range(0, len(lines), 3):
    part2 += badge_value(lines[i].strip(), lines[i+1].strip(), lines[i+2].strip())
print("Part 1: "+str(part1)+"\nPart 2: "+str(part2))