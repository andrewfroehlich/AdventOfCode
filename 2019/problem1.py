processed_lines = list((int(d)//3 - 2) for d in open("Resources/input1.txt"))
print("Part 1:",sum(processed_lines))

mass = 0
for my_mass in processed_lines:
    while my_mass > 0:
        mass += my_mass
        my_mass = my_mass//3 - 2
print("Part 2:",mass)