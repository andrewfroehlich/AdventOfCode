def build_dict():
    m = dict()
    lines = []
    for line in open("input21.txt").read().splitlines():
        spl = line.split()
        if len(spl) == 2:
            m[spl[0][0:-1]] = int(spl[1])
        else:
            lines.append(line)
    return m,lines
    
def reduce(m,lines):
    iterating = True
    while lines and "root" not in m and iterating:
        lines2 = []
        iterating = False
        for line in lines:
            spl = line.split()
            if spl[1] in m and spl[3] in m:
                iterating = True
                m[spl[0][0:-1]] = int(eval("".join([str(m[spl[1]]),spl[2],str(m[spl[3]])])))
            else:
                lines2.append(line)
        lines = lines2
    return m,lines

def part1():
    m,lines = build_dict()
    m,lines = reduce(m,lines)
    return m["root"]

def part2():
    m,lines = build_dict()
    del m["humn"]
    m,lines = reduce(m,lines)
    
    #now add remaining lines to dictionary as-is (with variable names)
    for line in lines:
        spl = line.split(": ")
        m[spl[0]] = spl[1]
    
    #starting with root, find the number and the variable we need to break down to get to humn
    spl = m["root"].split()
    num = int(m[spl[0]]) if m[spl[0]].isnumeric() else m[spl[2]]
    eq = m[spl[2]] if m[spl[0]].isnumeric() else m[spl[0]]
    
    #loop through the equations, keeping the number balanced, as we look for humn
    while eq != "humn" and len(eq.split()) > 1:
        spl = eq.split()
        if spl[0].isnumeric() or (spl[0] in m and isinstance(m[spl[0]],int)):
            eqnum = int(spl[0]) if spl[0].isnumeric() else m[spl[0]]
            eqvar = spl[2]
            var_first = False
        else: 
            eqnum = int(spl[2]) if spl[2].isnumeric() else int(m[spl[2]])
            eqvar = spl[0]
            var_first = True
        
        #process equation
        if spl[1] == "+":
            num -= eqnum
        elif spl[1] == "*":
            num = num // eqnum
        elif spl[1] == "-":
            if var_first:
                num += eqnum
            else:
                num = eqnum - num
        else: # division
            if var_first:
                num = num * eqnum
            else:
                num = eqnum // num
        
        #keep looping or return if humn is the variable
        if eqvar == "humn":
            return num
        else:
            eq = m[eqvar]

print("Part 1:",part1())
print("Part 2:",part2())