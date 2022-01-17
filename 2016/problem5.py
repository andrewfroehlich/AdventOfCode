import hashlib

s = "ffykfhsq"
i = 1
part1 = ""
part2 = ["" for _ in range(8)]
foundPart1 = False
while True:
    md5 = hashlib.md5((s+str(i)).encode("utf-8")).hexdigest()
    if md5[0:5] == "00000":
        if not foundPart1:
            part1 += md5[5:6]
            if len(part1) == 8:
                print("Part 1:",part1)
                foundPart1 = True
        position = int(md5[5:6]) if md5[5:6].isnumeric() else 10
        if position < 8 and part2[position] == "":
            part2[position] = md5[6:7]
            if "" not in part2:
                print("Part 2:","".join(part2))
                break
    i += 1