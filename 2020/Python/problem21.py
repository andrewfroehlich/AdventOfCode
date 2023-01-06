lines = open("../Resources/problem21.txt").read().splitlines()
allergens = dict() #allergen name to possible ingredients
foods = [] # arrays of [set of ingredients, set of allergens]
for line in lines:
    spl = line.split(" (contains ")
    ing = set(spl[0].split())
    alrg = set() if len(spl)==1 else set(spl[1][0:-1].split(", "))
    foods.append( [ing,alrg] )
    for a in alrg:
        if a in allergens:
            allergens[a] = allergens[a].intersection(ing)
        else:
            allergens[a] = ing

part1 = 0
allergen_possibilities = set()
for v in allergens.values():
    allergen_possibilities = allergen_possibilities.union(v)
for ing,alrg in foods:
    part1 += len( ing - allergen_possibilities )
print("Part 1:",part1)

ordered_allergens = list(allergens.keys())
ordered_allergens.sort()
ordered_dangerous_ing = [None for _ in range(len(ordered_allergens))]
found_ing = set()
while allergens:
    allergens2 = dict()
    for alrg,ing in allergens.items():
        ing = ing - found_ing
        if len(ing) == 1:
            index = ordered_allergens.index(alrg)
            ordered_dangerous_ing[index] = list(ing)[0]
            found_ing.add(ordered_dangerous_ing[index])
        else:
            allergens2[alrg] = ing
    allergens = allergens2.copy()
print("Part 2:",",".join(ordered_dangerous_ing))