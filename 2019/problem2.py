def run(in1, in2):
    computer = list(int(d) for d in open("Resources/input2.txt").readline().split(","))
    computer[1] = in1
    computer[2] = in2
    index = 0
    while index < len(computer):
        if computer[index] == 1:
            computer[computer[index+3]] = computer[computer[index+1]] + computer[computer[index+2]]
        elif computer[index] == 2:
            computer[computer[index+3]] = computer[computer[index+1]] * computer[computer[index+2]]
        elif computer[index] == 99:
            return computer[0]
        index += 4
    return computer[0]

def part2(output):
    for noun in range(0,100):
        for verb in range(0,100):
            if run(noun,verb) == output:
                return (100*noun)+verb

print("Part 1:",run(12,2),"\nPart 2:",part2(19690720))