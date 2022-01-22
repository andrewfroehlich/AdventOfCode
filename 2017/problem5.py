def run(part2):
    lines = open("Resources/input5.txt").readlines()
    index = steps = 0
    while index >= 0 and index < len(lines):
        next_index = index + int(lines[index])
        lines[index] = int(lines[index]) + (-1 if part2 and int(lines[index]) >= 3 else 1)
        index = next_index
        steps += 1
    return steps
print("Part 1:",run(False))
print("Part 2:",run(True))