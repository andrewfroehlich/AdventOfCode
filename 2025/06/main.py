import math

def part1():
    grid,part1 = [],0
    for line in open("input.txt"):
        try:
            current = [int(x) for x in line.split()]
            grid.append(current)
        except ValueError:
            symbols = line.split()
            for i, symbol in enumerate(symbols):
                column = [row[i] for row in grid]
                part1 += math.prod(column) if symbol == "*" else sum(column)
    return part1

def part2():
    input_lines = open("input.txt").readlines()
    symbols = input_lines[-1].split()
    total,curr_val,symbol_i = 0,0,0
    for i in range(max(len(line) for line in input_lines)):
        column = "".join(line[i] for line in input_lines[:-1])
        if column.strip() == "":
            if curr_val != 0:
                symbol_i += 1
            total += curr_val
            curr_val = 0
            continue
        next_int = int(column.strip())
        if curr_val == 0:
            curr_val = next_int
        else:
            curr_val = curr_val*next_int if symbols[symbol_i] == "*" else curr_val+next_int
    return total + curr_val

if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())