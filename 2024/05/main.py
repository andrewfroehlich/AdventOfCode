from collections import defaultdict

def process_input():
    rules_lines,update_lines = open("input.txt").read().split("\n\n")
    before = defaultdict(set) #specifies the set of values that must appear before the key if present
    for rule in rules_lines.split("\n"):
        first,second = [int(d) for d in rule.split("|")]
        before[second].add(first)
    return before, [[int(d) for d in order.split(",")] for order in update_lines.split("\n")]

def part1_value(before, order): #returns 0 if invalid, returns middle value if valid
    exists,seen = set(order),set()
    for current in order:
        if len( (before[current] & exists) - seen) > 0:
            return 0
        seen.add(current)
    return order[len(order)//2]

def part1(before, update_lines):
    return sum(part1_value(before,order) for order in update_lines)

def part2(before, update_lines):
    part2 = 0
    for order in update_lines:
        if part1_value(before,order) == 0:
            value_set,seen = set(order),set()
            result_order = []
            while value_set:
                for value in value_set:
                    if len((before[value] & (value_set | seen)) - seen) == 0:
                        result_order.append(value)
                        seen.add(value)
                value_set = value_set - seen
            part2 += result_order[len(result_order)//2]
    return part2

if __name__ == "__main__":
    before,update_lines = process_input()
    print("Part 1:",part1(before, update_lines))
    print("Part 2:",part2(before, update_lines))