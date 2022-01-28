def react(units):
    index = 0
    while index < len(units)-1:
        if ((units[index].islower() and units[index].upper() == units[index+1]) or 
            (units[index].isupper() and units[index].lower() == units[index+1])):
                units.pop(index)
                units.pop(index)
                index = index-1 if index>0 else 0
        else:
            index += 1
    return units

reacted = react(list(open("Resources/input5.txt").readline().strip()))
print("Part 1:",len(reacted))

min_length = len(reacted)
for i in range(26):
    units_str = "".join(reacted)
    units = list(units_str.replace(chr(ord('A')+i),'').replace(chr(ord('a')+i),''))
    reacted2 = react(units)
    min_length = min(min_length, len(reacted2))
print("Part 2:",min_length)