line = open("Resources/input9.txt").readline().strip()
nest = part1 = part2 = i = 0
garbage = False
while i < len(line):
    if garbage:
        if line[i] == "!":
            i += 1 #skip additional char
        elif line[i] == ">":
            garbage = False
        else:
            part2 += 1
    else:
        if line[i] == "{":
            nest += 1
        elif line[i] == "}":
            part1 += nest
            nest -= 1
        elif line[i] == "<":
            garbage = True
    i += 1
print("Part 1:",part1,"\nPart 2:",part2)