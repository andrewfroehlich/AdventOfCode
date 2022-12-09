def detect_unique(s, length):
    for i in range(length,len(s)):
        if len(set(s[i-length:i])) == length:
            return i

s = open("input6.txt").readline().strip()
print("Part 1:",detect_unique(s,4))
print("Part 2:",detect_unique(s,14))