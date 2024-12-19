from functools import cache

@cache
def run_remainder(pattern):
    if len(pattern) == 0:
        return 0
    return (1 if pattern in towels else 0) + sum(run_remainder(pattern[l:]) if pattern[0:0+l] in towels else 0 for l in range(1,max_towel+1))

def run(pattern_lines):
    results = [run_remainder(pattern) for pattern in pattern_lines.split("\n")]
    return sum(ans > 0 for ans in results), sum(results)

if __name__ == "__main__":
    towel_line,pattern_lines = open("input.txt").read().split("\n\n")
    towels = set(towel_line.split(", "))
    max_towel = max(len(t) for t in towels)
    part1,part2 = run(pattern_lines)
    print("Part 1:",part1,"\nPart 2:",part2)