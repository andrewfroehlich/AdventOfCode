from collections import defaultdict
from collections import deque

def mix_prune(x,y):
    return (x ^ y) % 16777216

def process(x):
    step1 = mix_prune(x, x*64)
    step2 = mix_prune(step1, step1//32)
    return mix_prune(step2, step2*2048)

def process_many(x, steps):
    for _ in range(steps):
        x = process(x)
    return x

def part1():
    return sum(process_many(int(secret),2000) for secret in open("input.txt"))

def part2():
    b = defaultdict(int)
    for secret in open("input.txt"):
        current_b,last_four = dict(),deque()
        sec = int(secret)
        for _ in range(2000):
            new_sec = process(sec)
            if len(last_four) >= 4: #don't pop if we haven't gotten up to four changes yet
                last_four.popleft()
            last_four.append((new_sec%10) - (sec%10))
            sec = new_sec
            if len(last_four) == 4 and tuple(last_four) not in current_b: #only update if we're four changes deep, and only the first instance
                current_b[tuple(last_four)] = sec%10

        for key,value in current_b.items(): #add all the possible bananas to the master sum list
            b[key] += value
    return max(b.values())

if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())