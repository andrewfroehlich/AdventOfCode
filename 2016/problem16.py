def get_checksum(a,target_len):
    while len(a) < target_len:
        b = list(a)
        b.reverse()
        a += "0"
        for c in b:
            a += "1" if c == "0" else "0"
    a = a[0:target_len]
    checksum = a
    while True:
        new_checksum = ""
        for i in range(len(checksum)//2):
            new_checksum += "1" if checksum[2*i] == checksum[2*i+1] else "0"
        checksum = new_checksum
        if len(checksum) % 2 > 0:
            return checksum
print("Part 1:",get_checksum("00111101111101000",272))
print("Part 2:",get_checksum("00111101111101000",35651584))