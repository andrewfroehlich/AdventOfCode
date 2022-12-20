def solve(dec_key=1,loops=1):
    identifier = 0
    nums,order = [],[]
    zero_obj = None
    for line in open("input20.txt").read().splitlines():
        ob = (int(line)*dec_key, identifier)
        if ob[0] == 0:
            zero_obj = ob
        nums.append(ob)
        order.append(ob)
        identifier += 1
    
    for loop in range(loops):
        for i in range(len(order)):
            num_index = nums.index(order[i])
            num = nums.pop(num_index)
            nums.insert(((num_index + num[0] + len(nums)) % len(nums)), num)

    ans = 0
    zero_index = nums.index(zero_obj)
    for j in (1000,2000,3000):
        ans += nums[((zero_index + j)%len(nums))][0]
    return ans

print("Part 1:",solve())
print("Part 2:",solve(811589153,10))