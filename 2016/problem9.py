def segment_count(segment, part2):
    count = i = 0
    while i < len(segment):
        inc = True
        if segment[i] == "(":
            next_end = segment[i:].find(')') + i
            if next_end > i:
                spl = segment[i+1:next_end].split("x")
                if len(spl) == 2 and spl[0].isnumeric() and spl[1].isnumeric():
                    inc = False
                    if part2:
                        count += int(spl[1]) * segment_count(segment[next_end+1:next_end+1+int(spl[0])], part2)
                    else:
                        count += int(spl[1]) * int(spl[0])
                    i = next_end+1+int(spl[0])
        if inc:
            count += 1
            i += 1
    return count

def decompress(part2):
    total = 0
    for line in open("Resources/input9.txt"):
        total += segment_count(line.strip(), part2)
    return total

print("Part 1:",decompress(False))
print("Part 2:",decompress(True))
