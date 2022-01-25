def part1(a,b):
    part1 = 0
    mod = 2**16
    for step in range(40000000):
        a = (a*16807)%2147483647
        b = (b*48271)%2147483647
        if a%mod == b%mod:
            part1 += 1
    return part1

def part2(a,b):
    part2 = 0
    mod = 2**16
    for step in range(5000000):
        a = (a*16807)%2147483647
        while a % 4 != 0:
            a = (a*16807)%2147483647
        b = (b*48271)%2147483647
        while b % 8 != 0:
            b = (b*48271)%2147483647
        if a%mod == b%mod:
            part2 += 1
    return part2

print("Part 1:",part1(591,393))
print("Part 2:",part2(591,393))