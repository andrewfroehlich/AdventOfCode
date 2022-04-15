rng = (265275,781584)
part1 = part2 = 0
current = rng[0]
while current <= rng[1]:
    arr = list(map(int, str(current)))
    adj1 = adj2 = False
    for i in range(1,len(arr)):
        if arr[i-1] > arr[i]:
            arr[i] = arr[i-1]
            for j in range(i+1,len(arr)):
                arr[j] = arr[j-1]
        if arr[i] == arr[i-1]:
            adj1 = True
            if ((i-1) == 0 or arr[i-2] != arr[i]) and (i == len(arr)-1 or arr[i+1] != arr[i]):
                adj2 = True
    current = int("".join(map(str,arr)))
    if adj1 and current <= rng[1]:
        part1 += 1
        if adj2:
            part2 += 1
    current += 1
print("Part 1:",part1,"\nPart 2:",part2)