target = {"children":3, "cats":7, "samoyeds":2, "pomeranians":3, "akitas":0, "vizslas":0, "goldfish":5, "trees":3, "cars":2, "perfumes":1}
for line in open("Resources/input16.txt"):
    line = line.replace(':', '').replace(',', '')
    _,num,key1,val1,key2,val2,key3,val3 = line.strip().split()
    keys = [key1,key2,key3]
    vals = [int(val1),int(val2),int(val3)]
    if target[keys[0]] == vals[0] and target[keys[1]] == vals[1] and target[keys[2]] == vals[2]:
        print("Part 1:",num)
    
    valid = True
    for i in range(len(keys)):
        if keys[i] in ("cats","trees"):
            valid = (vals[i] > target[keys[i]])
        elif keys[i] in ("pomeranians","goldfish"):
            valid = (vals[i] < target[keys[i]])
        else:
            valid = (vals[i] == target[keys[i]])
        if not valid:
            break
    if valid:
        print("Part 2:",num)