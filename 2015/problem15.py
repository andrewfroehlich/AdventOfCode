ingredients = []
for line in open("Resources/input15.txt"):
    _,_,c,_,d,_,f,_,t,_,cal = line.strip().split()
    this_ing = [int(val[:-1]) for val in [c,d,f,t]]
    this_ing.append(int(cal))
    ingredients.append(this_ing)

max_part1 = max_part2 = 0
for c0 in range(101):
    for c1 in range(101-c0):
        for c2 in range(101-c0-c1):
            for c3 in range(101-c0-c1-c2):
                nums = [c0,c1,c2,c3]
                score = 1
                cals = 0
                for ing in range(len(ingredients)):
                    cals += nums[ing]*ingredients[ing][-1]
                for prop in range(len(ingredients[0])-1):
                    current_property = 0
                    for ing in range(len(ingredients)):
                        current_property += nums[ing]*ingredients[ing][prop]
                    current_property = max(current_property,0)
                    score = score * current_property
                    if score == 0:
                        break
                max_part1 = max(max_part1, score)
                if cals == 500:
                    max_part2 = max(max_part2, score)
print("Part 1:",max_part1,"\nPart 2:",max_part2)