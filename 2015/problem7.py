class Wire():
    def __init__(self, line):
        spl = line.split()
        self.output = spl[-1]
        if spl[1] == "->":
            self.operation = "VALUE"
            self.input1 = spl[0]
            self.input2 = None
        elif spl[2] == "->":
            self.operation = spl[0]
            self.input1 = spl[1]
            self.input2 = None
        else:
            self.input1 = spl[0]
            self.operation = spl[1]
            self.input2 = spl[2]

wire_values = dict()    
def hasValue(inp):
    return inp.isnumeric() or inp in wire_values
def getValue(inp):
    return int(inp) if inp.isnumeric() else wire_values[inp]

def run(overrideB):
    global wire_values
    wire_values = dict()
    wires = []
    for line in open("Resources/input7.txt"):
        wires.append(Wire(line))
        if overrideB > -1 and wires[-1].output == "b":
            wires[-1].input1 = str(overrideB)

    while "a" not in wire_values:
        for index in range(len(wires)):
            w = wires[index]
            if not w: 
                continue
            if w.operation == "VALUE" and hasValue(w.input1):
                wire_values[w.output] = getValue(w.input1)
                wires[index] = None
            elif hasValue(w.input1) and (not w.input2 or hasValue(w.input2)):
                if w.operation == "NOT":
                    wire_values[w.output] = ~ getValue(w.input1)
                elif w.operation == "AND":
                    wire_values[w.output] = getValue(w.input1) & getValue(w.input2)
                elif w.operation == "OR":
                    wire_values[w.output] = getValue(w.input1) | getValue(w.input2)
                elif w.operation == "LSHIFT":
                    wire_values[w.output] = getValue(w.input1) << getValue(w.input2)
                elif w.operation == "RSHIFT":
                    wire_values[w.output] = getValue(w.input1) >> getValue(w.input2)
                wires[index] = None
    return wire_values["a"]

part1 = run(-1)
part2 = run(part1)
print("Part 1:",part1,"\nPart 2:",part2)