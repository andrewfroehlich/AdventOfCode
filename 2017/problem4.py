part1 = 0
for line in open("Resources/input4.txt"):
    words = set()
    valid = True
    for w in line.strip().split():
        if w in words:
            valid = False
            break
        words.add(w)
    part1 += 1 if valid else 0
print("Part 1:",part1)

part2 = 0
for line in open("Resources/input4.txt"):
    sorted_words = set()
    valid = True
    for w in line.strip().split():
        w_list = list(w)
        w_list.sort()
        sorted_w = "".join(w_list)
        if sorted_w in sorted_words:
            valid = False
            break
        sorted_words.add(sorted_w)
    part2 += 1 if valid else 0
print("Part 2:",part2)