def part1(lines):
    twos = threes = 0
    for box in lines:
        l = list(box.strip())
        l.sort()
        l.append("_") #lets the loop catch the last letter
        hasTwo = hasThree = False
        letter = l[0]
        letter_count = 1
        for i in range(1,len(l)):
            if l[i] == letter:
                letter_count += 1
            else:
                if letter_count == 2:
                    hasTwo = True
                elif letter_count == 3:
                    hasThree = True
                letter = l[i]
                letter_count = 1
        twos += 1 if hasTwo else 0
        threes += 1 if hasThree else 0
    return twos*threes

def part2(lines):
    for a in range(len(lines)-1):
        for b in range(a+1,len(lines)):
            for i in range(len(lines[a])):
                if (lines[a][:i]+lines[a][i+1:]).strip() == (lines[b][:i]+lines[b][i+1:]).strip():
                    return (lines[a][:i]+lines[a][i+1:]).strip()

lines = open("Resources/input2.txt").readlines()
print("Part 1:",part1(lines))
print("Part 2:",part2(lines))