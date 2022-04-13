def ex(code,a,b,c,reg):
    if code[0:3] == "add":
        return reg[a] + (reg[b] if code[-1] == "r" else b)
    elif code[0:3] == "mul":
        return reg[a] * (reg[b] if code[-1] == "r" else b)
    elif code[0:3] == "ban":
        return reg[a] & (reg[b] if code[-1] == "r" else b)
    elif code[0:3] == "bor":
        return reg[a] | (reg[b] if code[-1] == "r" else b)
    elif code[0:3] == "set":
        return (reg[a] if code[-1] == "r" else a)
    elif code[0:2] == "gt":
        return 1 if ((reg[a] if code[2:3] == "r" else a) > (reg[b] if code[-1] == "r" else b)) else 0
    else: #eq
        return 1 if ((reg[a] if code[2:3] == "r" else a) == (reg[b] if code[-1] == "r" else b)) else 0

lines = open("Resources/input16-a.txt").readlines()
ops = {"addr","addi","mulr","muli","banr","bani","borr","bori","setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"}
op_map = dict()
for i in range(16):
    op_map[i] = ops.copy()
index = part1 = 0
while index < len(lines):
    matches = 0
    bef_arr = list(int(d) for d in lines[index][9:19].split(", "))
    bef_reg = {0:bef_arr[0],1:bef_arr[1],2:bef_arr[2],3:bef_arr[3]}
    opcode = list(int(d) for d in lines[index+1].split())
    aft_arr = list(int(d) for d in lines[index+2][9:19].split(", "))
    for op in ops:
        op_match = True
        c_val = ex(op,opcode[1],opcode[2],opcode[3],bef_reg)
        for i in range(4):
            if aft_arr[i] != (c_val if opcode[3] == i else bef_arr[i]):
                op_match = False
                op_map[opcode[0]].discard(op)
        if op_match:
            matches += 1
            if matches == 3:
                part1 += 1
    index += 4
print("Part 1:",part1)

#Using the map of possible ops per op-code, find the true op per op-code
ops_set = 0
op_arr = list("" for _ in range(16))
while ops_set < 16:
    for op_id in range(16):
        if not op_arr[op_id] and len(op_map[op_id]) == 1:
            op_found = list(op_map[op_id])[0]
            op_arr[op_id] = op_found
            ops_set += 1
            for i in range(16):
                op_map[i].discard(op_found)

#Run the code with the found op codes
reg = {0:0,1:0,2:0,3:0}
for line in open("Resources/input16-b.txt"):
    opcode = list(int(d) for d in line.strip().split())
    reg[opcode[3]] = ex(op_arr[opcode[0]],opcode[1],opcode[2],opcode[3],reg)
print("Part 2:",reg[0])