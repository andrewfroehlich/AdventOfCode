import itertools

def maxArrangement(names,values):
    max_value = 0
    for perm in itertools.permutations(names):
        current_value = 0
        for i in range(len(perm)-1):
            current_value += values[(perm[i],perm[i+1])]
            current_value += values[(perm[i+1],perm[i])]
        current_value += values[(perm[-1],perm[0])]
        current_value += values[(perm[0],perm[-1])]
        max_value = max(max_value,current_value)
    return max_value

values = dict()
names = set()
for line in open("Resources/input13.txt"):
    n1,_,mult,val,*_,n2 = line.strip()[:-1].split()
    values[(n1,n2)] = int(val) if mult == "gain" else -1*int(val)
    names.add(n1)
print("Part 1:",maxArrangement(names,values))

names.add("Me")
for n in names:
    values[(n,"Me")] = 0
    values[("Me",n)] = 0
print("Part 2:",maxArrangement(names,values))