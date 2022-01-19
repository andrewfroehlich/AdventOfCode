from collections import defaultdict

def part1(elves):
    presents = defaultdict(lambda:1)
    elf_index = 0
    while True:
        if presents[elf_index] != 0:
            target_elf = (elf_index+1)%elves
            while presents[target_elf] == 0:
                target_elf = (target_elf + 1) % elves
            presents[elf_index] += presents[target_elf]
            presents[target_elf] = 0
        if presents[elf_index] == elves:
            return elf_index+1
        elf_index = (elf_index+1)%elves

def part2(elves):
    presents = []
    for i in range(elves):
        presents.append(i+1) #elf number
    elf_index = 0
    while len(presents) > 1:
        to_remove = (elf_index + (len(presents)//2)) % len(presents)
        presents.pop(to_remove)
        elf_index = ((elf_index) if to_remove < elf_index else (elf_index+1)) % len(presents)
    return presents[0]

print("Part 1:",part1(3017957))
print("Part 2:",part2(3017957))