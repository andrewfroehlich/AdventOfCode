def part1():
    dial,zeroes = 50,0
    for line in open("input.txt"):
        dial = (dial + ((-1 if line[0] == "L" else 1) * int(line[1:])) + 10000) % 100
        zeroes += (1 if dial == 0 else 0)
    return zeroes

def part2():
    dial,zeroes = 50,0
    for line in open("input.txt"):
        direction,distance = line[0],int(line[1:])
        if direction == "R":
            zeroes += (dial + distance) // 100
        else:
            zeroes += distance // 100 + (1 if (distance % 100 >= dial > 0) else 0)
        dial = (dial + ((-1 if direction == "L" else 1) * distance) + 10000) % 100
    return zeroes

if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())