from functools import cache

@cache
def usable_factors(n):
    return [i for i in range(1, n // 2 + 1) if n % i == 0]

def part1():
    part1 = 0
    for part in open("input.txt").read().split(","):
        low,high = map(int, part.split("-"))
        first_half = str(low)[:len(str(low))//2] or "0"
        current = int(2*first_half)
        while current <= high:
            if current >= low:
                part1 += current
            first_half = str(int(first_half)+1)
            current = int(2*first_half)
    return part1

def part2():
    part2 = set()
    for part in open("input.txt").read().split(","):
        low,high = map(int, part.split("-"))
        current = low
        while current <= high:
            curr_len = len(str(current))
            for factor_size in usable_factors(curr_len):
                pattern = str(current)[:factor_size]
                reps = curr_len // factor_size
                inner_current = int(pattern*reps)
                while inner_current <= high:
                    if inner_current >= low:
                        part2.add(inner_current)
                    pattern = str(int(pattern)+1)
                    inner_current = int(pattern*reps)
            current = int("1" + "0"*curr_len)
    return sum(part2)

if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())