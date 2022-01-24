def run_hash(nums, lengths, index, skip):
    for l in lengths:
        for i in range(l//2):
            temp = nums[(index+i)%len(nums)]
            nums[(index+i)%len(nums)] = nums[(index+l-1-i)%len(nums)]
            nums[(index+l-1-i)%len(nums)] = temp
        index = (index + l + skip) % len(nums)
        skip += 1
    return nums,index,skip

nums = [i for i in range(256)]
lengths = [int(l) for l in open("Resources/input10.txt").readline().split(",")]
part1_nums,_,_ = run_hash(nums, lengths, 0, 0)
print("Part 1:",part1_nums[0]*part1_nums[1])

nums = [i for i in range(256)]
lengths = [ord(c) for c in open("Resources/input10.txt").readline().strip()]
lengths.extend([17,31,73,47,23])
index = skip = 0
for j in range(64):
    nums,index,skip = run_hash(nums, lengths, index, skip)
dense_hash = []
for i in range(16):
    result = nums[16*i]
    for j in range(1,16):
        result = result ^ nums[16*i + j]
    dense_hash.append(result)
print("Part 2:", "".join([hex(n)[-2:] for n in dense_hash]))