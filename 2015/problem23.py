def run(lines, a, b):
    registers = {"a":a, "b":b}
    index = 0
    while index < len(lines) and index >= 0:
        instruction = lines[index].strip().replace(',','').split()
        index += 1
        if instruction[0] == "inc":
            registers[instruction[1]] += 1
        elif instruction[0] == "tpl":
            registers[instruction[1]] *= 3
        elif instruction[0] == "hlf":
            registers[instruction[1]] = registers[instruction[1]]//2
        elif instruction[0] == "jmp":
            index += int(instruction[1]) - 1 # 1 already added, remove
        elif instruction[0] == "jie":
            if registers[instruction[1]] % 2 == 0:
                index += int(instruction[2]) - 1 # 1 already added, remove
        else: #jio
            if registers[instruction[1]] == 1:
                index += int(instruction[2]) - 1 # 1 already added, remove
    return registers["b"]

lines = open("Resources/input23.txt").readlines()
print("Part 1:",run(lines,0,0))
print("Part 2:",run(lines,1,0))