def run(input_val):
    computer = list(int(d) for d in open("Resources/input5.txt").readline().split(","))
    index = 0
    while index < len(computer):
        instr = computer[index]
        opcode = instr % 100
        if opcode in (1,2,7,8):
            p1 = computer[index+1] if (instr%1000)//100 == 1 else computer[computer[index+1]]
            p2 = computer[index+2] if (instr%10000)//1000 == 1 else computer[computer[index+2]]
            if opcode == 1:
                computer[computer[index+3]] = p1+p2
            elif opcode == 2:
                computer[computer[index+3]] = p1*p2
            elif opcode == 7:
                computer[computer[index+3]] = 1 if p1<p2 else 0
            else:
                computer[computer[index+3]] = 1 if p1==p2 else 0
            index += 4
        elif opcode == 3:
            computer[computer[index+1]] = input_val
            index += 2
        elif opcode == 4:
            output = computer[index+1] if (instr%1000)//100 == 1 else computer[computer[index+1]]
            if output != 0:
                return output
            index += 2
        elif opcode in (5,6):
            p1 = computer[index+1] if (instr%1000)//100 == 1 else computer[computer[index+1]]
            if (opcode == 5 and p1 != 0) or (opcode == 6 and p1 == 0):
                index = computer[index+2] if (instr%10000)//1000 == 1 else computer[computer[index+2]]
            else:
                index += 3
        elif opcode == 99:
            break    
    
print("Part 1:", run(1))
print("Part 2:", run(5))