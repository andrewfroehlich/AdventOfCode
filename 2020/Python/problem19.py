import re

rules,messages = open("../Resources/problem19.txt").read().split("\n\n")
rules = rules.splitlines()
messages = messages.splitlines()

# raw_map has raw rules that still reference other rules. reduced is just rules boiled down to a's and b's. Initially, only the "a" and "b" rule are in reduced.
raw_map,reduced = dict(),dict()
for rule in rules:
    spl = rule.split(": ")
    if spl[1] in ("\"a\"","\"b\""):
        reduced[spl[0]] = spl[1][1]
    else:
        raw_map[spl[0]] = spl[1]

# Loop through the raw_map trying to reduce the rule references. Only move to reduced if the rule is fully-reduced, meaning it has no numeric references left
while raw_map:
    raw_map2 = dict()
    for k,v in raw_map.items():
        elements = v.split()
        fully_reduced = True
        for i in range(len(elements)):
            if elements[i] in reduced:
                elements[i] = reduced[elements[i]]
            elif elements[i].isnumeric():
                fully_reduced = False
        
        reduced_text = " ".join(elements) #leave spaces between for splits
        if "|" in elements:
            reduced_text = "( " + reduced_text + " )"
        if fully_reduced:
            reduced[k] = reduced_text
        else:
            raw_map2[k] = reduced_text
    raw_map = raw_map2.copy()

regex = re.compile("^"+reduced["0"].replace(" ","")+"$")
part1 = 0
for m in messages:
    if regex.match(m):
        part1 += 1
print("Part 1:",part1)


# 0 effectively becomes (42)+(42 11* 31), or (42)+(42){n}(31){n} where n>0. There isn't an effective way to represent this as a regex, so creating a regex for the first 5 values of n and checking all
reduced["42"] = reduced["42"].replace(" ","")
reduced["31"] = reduced["31"].replace(" ","")
regex = []
for repeats in range(5):
    regex.append(re.compile("^("+reduced["42"]+")+("+reduced["42"]+"){"+str(1+repeats)+"}("+reduced["31"]+"){"+str(1+repeats)+"}$"))
part2 = 0
for m in messages:
    for reg in regex:
        if reg.match(m):
            part2 += 1
            break
print("Part 2:",part2)