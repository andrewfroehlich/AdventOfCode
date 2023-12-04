import re
from collections import deque

def solve():
    sum1 = sum2 = 0
    bonus_buffer = deque()
    for line in open("input.txt"):
        nums = line.split(": ")[1].split(" | ")
        winners = set([int(d) for d in re.findall("\\d+", nums[0])])
        found = sum([1 for n in re.findall("\\d+", nums[1]) if int(n) in winners])
        
        # Part 1
        sum1 += 2 ** (found - 1) if found > 0 else 0
        
        # Part 2 
        multiple = 1 + (bonus_buffer.popleft() if bonus_buffer else 0)
        sum2 += multiple
        for i in range(found):
            if len(bonus_buffer) > i:
                bonus_buffer[i] += multiple
            else:
                bonus_buffer.append(multiple)
    return sum1,sum2

if __name__ == '__main__':
    p1,p2 = solve()
    print("Part 1:", p1)
    print("Part 2:", p2)