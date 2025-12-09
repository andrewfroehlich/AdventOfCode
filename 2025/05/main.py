def parse():
    fresh_ranges,to_check = open("input.txt").read().split("\n\n")
    ranges = [tuple(map(int, line.split("-"))) for line in fresh_ranges.splitlines()]
    ids = [int(line) for line in to_check.splitlines()]
    return ranges, ids

def is_fresh(num,ranges):
    for low,high in ranges:
        if low <= num <= high:
            return True
    return False

def part1(ranges,ids):
    return sum(1 for num in ids if is_fresh(num,ranges))

def part2(ranges):
    sorted_ranges = sorted(ranges)
    merged = [sorted_ranges[0]]
    for low,high in sorted_ranges[1:]:
        last_low,last_high = merged[-1]
        if low <= last_high + 1:
            merged[-1] = (last_low, max(high, last_high))
        else:
            merged.append((low, high))
    return sum(high-low+1 for low,high in merged)

if __name__ == "__main__":
    ranges,ids = parse()
    print("Part 1:",part1(ranges,ids))
    print("Part 2:",part2(ranges))