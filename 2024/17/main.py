def process_input():
    var_lines,program_line = open("input.txt").read().split("\n\n")
    vars = [int(d.split(": ")[1]) for d in var_lines.split("\n")]
    program = [int(d) for d in program_line.split(": ")[1].split(",")]
    return vars,program

def combo(vars,operand):
    return vars[operand-4] if 4 <= operand <= 6 else operand

def run_program(vars,program,is_part2):
    i,out = 0,[]
    while i + 1 < len(program):
        inst,operand = program[i],program[i+1]
        match inst:
            case 0: #adv
                vars[0] = int(vars[0] / (2**combo(vars,operand)))
            case 1: #bxl
                vars[1] ^= operand
            case 2: #bst
                vars[1] = combo(vars,operand) % 8
            case 3: #jnz
                if vars[0] != 0:
                    i = operand
                    continue
                elif is_part2: # don't loop back if it's part 2, just return output
                    return out
            case 4: #bxc
                vars[1] ^= vars[2]
            case 5: #out
                out.append( int(combo(vars,operand) % 8) )
            case 6: #bdv
                vars[1] = int(vars[0] / (2**combo(vars,operand)))
            case 7: #cdv
                vars[2] = int(vars[0] / (2**combo(vars,operand)))
        i = i+2
    return ",".join(str(d) for d in out)

def part2(program, a, reverse_index):
    target_val = program[-reverse_index]
    for i in range(0, 8):
        out = run_program([a+i,0,0],program,True)
        if out[0] == target_val:
            if reverse_index == len(program):
                return a+i
            else:
                return part2(program, (a+i) * 8, reverse_index+1)

if __name__ == "__main__":
    vars,program = process_input()
    print("Part 1:",run_program(vars,program,False))
    print("Part 2:",part2(program, 0, 1))