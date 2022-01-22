checksum1 = checksum2 = 0
for line in open("Resources/input2.txt"):
    nums = [int(d) for d in line.split()]
    nums.sort()
    nums.reverse()
    checksum1 += nums[0] - nums[-1]
    multiple = -1
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] % nums[j] == 0:
                multiple = nums[i] // nums[j]
        if multiple > -1:
            break
    checksum2 += multiple
print("Part 1:",checksum1,"\nPart 2:",checksum2)