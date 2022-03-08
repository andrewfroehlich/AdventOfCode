def solve(target):
    recipes = [3,7]
    index1,index2,target_index = 0,1,0
    target_str = str(target)
    part1 = ""
    while len(recipes) <= target + 10 or target_index < len(target_str):
        new_recipe = recipes[index1]+recipes[index2]
        for c in str(new_recipe):
            recipes.append(int(c))
            if c == target_str[target_index]:
                target_index += 1
                if target_index == len(target_str):
                    return part1,len(recipes)-len(target_str)
            else:
                target_index = 0
        index1 = (index1 + 1 + recipes[index1]) % len(recipes)
        index2 = (index2 + 1 + recipes[index2]) % len(recipes)
        
        if not part1 and len(recipes) > target + 10:
            result = []
            for i in range(target,target+10):
                result.append(str(recipes[i]))
            part1 = "".join(result)

part1,part2 = solve(704321)
print("Part 1:",part1,"\nPart 2:",part2)