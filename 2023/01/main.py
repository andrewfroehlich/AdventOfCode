def part1():
    sum1 = 0
    for line in open("input.txt"):
        for i_l in range(len(line)):
            if "0" <= line[i_l] <= "9":
                sum1 += (10 * int(line[i_l]))
                break
        for i_r in range(len(line)-1, -1, -1):
            if "0" <= line[i_r] <= "9":
                sum1 += int(line[i_r])
                break
    return sum1

def part2():
    sum2 = 0
    valid_tree = {
        "1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
        "o":{"n":{"e":1}},
        "t":{"w":{"o":2},"h":{"r":{"e":{"e":3}}}},
        "f":{"o":{"u":{"r":4}},"i":{"v":{"e":5}}},
        "s":{"i":{"x":6},"e":{"v":{"e":{"n":7}}}},
        "e":{"i":{"g":{"h":{"t":8}}}},
        "n":{"i":{"n":{"e":9}}}
    }
    for line in open("input.txt"):
        l = r = -1
        for i in range(len(line)):
            current = valid_tree
            if line[i] in current:
                current = current[line[i]]
                j = i+1
                while not (isinstance(current, int) or j==len(line) or line[j] not in current):
                    current = current[line[j]]
                    j = j+1
                if isinstance(current, int):
                    if l == -1:
                        l = current
                    r = current
        sum2 += (10 * l) + r
    return sum2

if __name__ == "__main__":
    print("Part 1:",part1())
    print("Part 2:",part2())