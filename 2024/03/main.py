import re

def part1(text):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, text)
    return sum([(int(x) * int(y)) for x, y in matches])

def part2(text):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)'
    matches = re.finditer(pattern, text)

    enabled = True
    part2 = 0
    for match in matches:
        if match.group() == 'do()':
            enabled = True
        elif match.group() == "don't()":
            enabled = False
        elif match.group().startswith('mul') and enabled:
            x, y = match.groups()
            part2 += int(x) * int(y)
    return part2

if __name__ == "__main__":
    input = open("input.txt").read()
    print("Part 1:",part1(input))
    print("Part 2:",part2(input))