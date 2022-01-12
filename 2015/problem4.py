import hashlib

s = "iwrupvqb"
i = 1
foundPart1 = False
while True:
    md5 = hashlib.md5(("{}{}".format(s,i)).encode("utf-8")).hexdigest()
    if not foundPart1 and md5[0:5] == "00000":
        print("Part 1:",i)
        foundPart1 = True
    if md5[0:6] == "000000":
        print("Part 2:",i)
        break
    i += 1