def getValue(var, register):
    return int(var) if var.strip("-").isnumeric() else register[var]

def run(a,b,c,d):
    register = {"a":a, "b":b, "c":c, "d":d}
    lines = open("Resources/input23.txt").readlines()
    index = 0
    current_b = 0
    while index >= 0 and index < len(lines):
        if register["b"] != current_b:
            print(register["a"],register["b"],register["c"],register["d"])
            current_b = register["b"]
        line = lines[index].strip()
        if line[0:3] == "inc":
            register[line.split()[1]] += 1
            index += 1
        elif line[0:3] == "dec":
            register[line.split()[1]] -= 1
            index += 1
        elif line[0:3] == "tgl":
            val = getValue(line.split()[1], register)
            if index+val >= 0 and index+val < len(lines):
                line_to_change = lines[index+val]
                if line_to_change[0:3] == "inc":
                    lines[index+val] = line_to_change.replace("inc","dec",1)
                elif line_to_change[0:3] == "jnz":
                    lines[index+val] = line_to_change.replace("jnz","cpy",1)
                elif line_to_change[0:3] == "cpy":
                    lines[index+val] = line_to_change.replace("cpy","jnz",1)
                else: # line_to_change[0:3] in ("dec","tgl"):
                    lines[index+val] = line_to_change.replace("dec","inc",1).replace("tgl","inc",1)
            index += 1
        else:
            inst,x,y = line.split()
            if inst == "cpy":
                if y in register:
                    register[y] = getValue(x,register)
                index += 1
            else: #jnz
                index += getValue(y,register) if getValue(x,register) != 0 else 1
    return register["a"]

#print("Part 1:",run(7,0,0,0))
print("Part 2:",run(12,0,0,0))