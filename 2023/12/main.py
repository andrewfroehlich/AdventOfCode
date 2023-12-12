from itertools import combinations
from functools import cache

def part1():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    sum1 = 0
    for line in lines:
        puzzle,numbers_raw = line.split()
        numbers = [int(d) for d in numbers_raw.split(",")]
        blanks = [i for i, c in enumerate(puzzle) if c == "?"]
        damaged = [i for i, c in enumerate(puzzle) if c == "#"]
        extra_damaged = sum(numbers) - len(damaged)
        for new_damaged in combinations(blanks, extra_damaged):
            new_damaged = list(new_damaged) + damaged
            new_damaged.sort()
            new_numbers = [1]
            for i in range(1,len(new_damaged)):
                if new_damaged[i] == new_damaged[i-1]+1:
                    new_numbers[-1] += 1
                else:
                    new_numbers.append(1)
            if new_numbers == numbers:
                sum1 += 1
    return sum1

def part1_recurse():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    sum1 = 0
    for line in lines:
        puzzle,numbers_raw = line.split()
        numbers = [int(d) for d in numbers_raw.split(",")]
        sum1 += recurse(puzzle, tuple(numbers), 0)
    return sum1

def part2():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    sum2 = 0
    line_num = 0
    for line in lines:
        puzzle,numbers_raw = line.split()
        puzzle = 5*(puzzle + "?")
        puzzle = puzzle[:-1]
        numbers = [int(d) for d in numbers_raw.split(",")]
        numbers = 5*numbers
        sum2 += recurse(puzzle, tuple(numbers), 0)
    return sum2

@cache
# line is the puzzle still left to process
# numbers is the groups of gears we still need to find (tuple, to be cachable)
# buffer_size is the size of the current gear we are looking at, as we move 1 char at a time
def recurse(line, numbers, buffer_size):
    # base (no line left)
    if len(line) == 0:
        if len(numbers) == 1 and numbers[0] == buffer_size:
            return 1 # final group matches the buffer, so match
        elif len(numbers) == 0 and buffer_size == 0:
            return 1 # nothing left to find so this counts
        else:
            return 0 # other cases shouldn't match if we ran out of line
    # failure 
    if len(numbers) == 0 and buffer_size > 0:
        return 0 # we have a gear in the buffer that matches nothing
    elif len(numbers) > 0 and numbers[0] < buffer_size:
        return 0 # too big
    # success/continuation
    n = 0
    if line[0] == "#" or line[0] == "?":
        n += recurse(line[1:], numbers, buffer_size+1)
    if line[0] == "." or line[0] == "?": # catch ? in both cases, count for both possibilities
        if buffer_size == 0: #start a new one
            n += recurse(line[1:], numbers, 0) #move forward
        elif len(numbers) > 0 and numbers[0] == buffer_size:
            n += recurse(line[1:], numbers[1:], 0) #advance to the next number
    return n

if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 1 Recursive:",part1_recurse())
    print("Part 2:",part2())