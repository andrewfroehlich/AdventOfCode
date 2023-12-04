import re
from collections import deque

def part1():
    sum1 = 0
    for line in open("input.txt"):
        nums = line.strip().split(": ")[1].split(" | ")
        winners = set([int(d) for d in re.findall("\\d+", nums[0])])
        power = sum([1 for n in re.findall("\\d+", nums[1]) if int(n) in winners]) - 1
        sum1 += 2 ** power if power > -1 else 0
    return sum1

def part2():
    sum2 = 0
    bonus_buffer = deque()
    for line in open("input.txt"):
        multiple = 1
        if bonus_buffer:
            multiple += bonus_buffer.popleft()
        sum2 += multiple
        nums = line.strip().split(": ")[1].split(" | ")
        winners = set([int(d) for d in re.findall("\\d+", nums[0])])
        found = sum([1 for n in re.findall("\\d+", nums[1]) if int(n) in winners])
        for i in range(found):
            if len(bonus_buffer) > i:
                bonus_buffer[i] = bonus_buffer[i] + multiple
            else:
                bonus_buffer.append(multiple)
    return sum2

if __name__ == '__main__':
    print("Part 1:", part1())
    print("Part 2:", part2())