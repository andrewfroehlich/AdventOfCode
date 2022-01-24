from collections import defaultdict

reg = defaultdict(int)
part1 = part2 = 0
for line in open("Resources/input8.txt"):
    #print(line)
    var,incdec,val,_,exec_var,exec_con,exec_val = line.strip().split()
    exec_str = "{}{}{}".format(reg[exec_var],exec_con,exec_val)
    if bool(eval(exec_str)):
        reg[var] += int(val) if incdec == "inc" else -int(val)
        part2 = max(part2, reg[var])
for k,v in reg.items():
    part1 = max(part1,v)
print("Part 1:",part1,"\nPart 2:",part2)