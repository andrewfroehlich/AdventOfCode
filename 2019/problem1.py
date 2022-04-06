mass = 0
for line in open("Resources/input1.txt"):
    mass += int(line)//3 - 2
print("Part 1:",mass)

mass = 0
for line in open("Resources/input1.txt"):
    my_mass = int(line)//3 - 2
    while my_mass > 0:
        mass += my_mass
        my_mass = my_mass//3 - 2
print("Part 2:",mass)
    