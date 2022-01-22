def getValue(var, register):
    return int(var) if var.strip("-").isnumeric() else register[var]

def run(a,b,c,d):
    register = {"a":a, "b":b, "c":c, "d":d}
    lines = open("Resources/input25.txt").readlines()
    index = 0
    outputs = 0
    while index >= 0 and index < len(lines):
        line = lines[index].strip()
        if line[0:3] == "inc":
            register[line.split()[1]] += 1
            index += 1
        elif line[0:3] == "dec":
            register[line.split()[1]] -= 1
            index += 1
        elif line[0:3] == "out":
            outputs += 1
            val = getValue(line.split()[1], register)
            index += 1
            if (outputs+1)%2 != val:
                return False
            if outputs > 100:
                return True
        else:
            inst,x,y = line.split()
            if inst == "cpy":
                register[y] = getValue(x,register)
                index += 1
            else: #jnz
                index += getValue(y,register) if getValue(x,register) != 0 else 1
    return False

found = False
part1 = 0
while not found:
    part1+=1
    found = run(part1,0,0,0)
print("Part 1:",part1)