from collections import deque

plants = set()
inp = open("Resources/input12.txt").readlines()
initial_state = inp[0].split(": ")[1].strip()
for i in range(len(initial_state)):
    if initial_state[i] == "#":
        plants.add(i)
notes = set()
for j in range(2,len(inp)):
    src,dst = inp[j].strip().split(" => ")
    if dst == "#":
        notes.add(src)

buffer = deque(list("....."))
for gen in range(2000):
    new_plants = set()
    for i in range(min(plants)-2,max(plants)+3):
        buffer.popleft()
        if (i+2) in plants:
            buffer.append("#")
        else:
            buffer.append(".")
        
        if "".join(buffer) in notes:
            new_plants.add(i)
    plants = new_plants
    if gen == 19:
        print("Part 1:",sum(plants))
    if gen % 100 == 99:
        print("Gen={}, Plant Count={}, Sum={}".format(gen+1,len(plants),sum(plants)))
#From looking at the results over time, the plant count remains the same, they just shift to the right. The sum
#follows the pattern of sum = 8898 + 81*(gen-100). Putting 50 billion into this formula yields the part 2 answer
print("Part 2:",8898 + 81*(50000000000-100))