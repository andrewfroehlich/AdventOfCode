containers = [int(c) for c in open("Resources/input17.txt").readlines()]
containers_used = dict.fromkeys(range(1,21),0)
for b in range(2 ** 20):
    current_sum,current_containers = 0,0
    if bin(b)[-1] == "1":
        current_sum = containers[-1]
        current_containers = 1
    for i in range(2, len(containers)+1):
        if bin(b)[-i:-i+1] == "1":
            current_sum += containers[-i]
            current_containers += 1
        elif bin(b)[-i:-i+1] == "b":
            break
    if current_sum == 150:
        containers_used[current_containers] += 1

part1 = part2 = 0
for i in range(1,len(containers)+1):
    part1 += containers_used[i]
    if containers_used[i] > 0 and part2 == 0:
        part2 = containers_used[i]
print("Part 1:",part1,"\nPart 2:",part2)