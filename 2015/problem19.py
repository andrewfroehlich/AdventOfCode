lines = open("Resources/input19.txt").readlines()
translations = dict()
for l in range(len(lines)-2):
    src,out = lines[l].strip().split(" => ")
    if src in translations:
        translations[src].append(out)
    else:
        translations[src] = [out]

#Part 1
molecule = []
for c in lines[-1].strip():
    if c.isupper():
        molecule.append(c)
    else:
        molecule[-1] = molecule[-1]+c

translated = set()
for i in range(len(molecule)):
    temp = molecule[i]
    if temp not in translations:
        continue
    for step in translations[temp]:
        molecule[i] = step
        translated.add("".join(molecule))
        molecule[i] = temp
print("Part 1:",len(translated))

#Part 2
rev_tran = dict()
outputs = []
for l in range(len(lines)-2):
    src,out = lines[l].strip().split(" => ")
    rev_tran[out] = src
    outputs.append(out)
outputs.sort(key=len)
outputs.reverse()

steps = 0
molecule = lines[-1].strip()
while molecule not in translations["e"]:
    steps += 1
    for o in outputs:
        if o in molecule:
            molecule = molecule.replace(o, rev_tran[o], 1)
            break
print("Part 2:",steps+1)