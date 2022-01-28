from collections import defaultdict

raw_input = open("Resources/input25.txt").readlines()
state = ""
line_index = steps = 0
rules = dict() 
while line_index < len(raw_input):
    line = raw_input[line_index].strip()
    line_index += 1
    if not line:
        continue
    elif line[0:5] == "Begin":
        state = line[-2:-1]
    elif line[0:7] == "Perform":
        steps = int(line.split()[5])
    else:
        # (current 0: (write, moveLeft, newState), current 1: (write, moveLeft, newState))
        rules[line[-2:-1]] = ( (
            int(raw_input[line_index+1].strip()[-2:-1]),
            "left" in raw_input[line_index+2],
            raw_input[line_index+3].strip()[-2:-1]), (
            int(raw_input[line_index+5].strip()[-2:-1]),
            "left" in raw_input[line_index+6],
            raw_input[line_index+7].strip()[-2:-1]) )
        line_index += 8

tape = defaultdict(bool)
tape_index = 0
for _ in range(steps):
    rules_0,rules_1 = rules[state]
    write,moveLeft,newState = rules_1 if tape[tape_index] else rules_0
    tape[tape_index] = True if write==1 else False
    tape_index += -1 if moveLeft else 1
    state = newState
print("Part 1:",sum(1 for v in tape.values() if v))