from collections import Counter

part1 = 0
for line in open("Resources/input4.txt"):
    spl = line.strip().split("-")
    char_list = []
    for i in range(len(spl)-1):
        char_list.extend(list(spl[i]))
    char_list.sort()
    c = Counter(char_list)
    common = "".join([k[0] for k in c.most_common(5)])
    if common == spl[-1][-6:-1]:
        sector_id = int(spl[-1].split("[")[0])
        part1 += sector_id
        
        new_string = []
        for i in range(len(spl)-1):
            new_word = []
            for c in spl[i]:
                new_word.append(chr((ord(c) - ord('a') + sector_id)%26 + ord('a')))
            new_string.append("".join(new_word))
        s = " ".join(new_string)
        if "north" in s or "pole" in s:
            print("Part 2: {} is sector {}".format(s,sector_id))
print("Part 1:",part1)
