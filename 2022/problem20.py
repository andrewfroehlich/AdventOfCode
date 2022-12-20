def solve(dec_key=1,loops=1):
    i = 0
    nums,order = [],[]
    zero_obj = None
    for line in open("input20.txt").read().splitlines():
        ob = (int(line)*dec_key,i)
        if ob[0] == 0:
            zero_obj = ob
        nums.append(ob)
        order.append(ob)
        i += 1
    
    for loop in range(loops):
        for i in range(len(order)):
            num_index = nums.index(order[i])
            num = nums.pop(num_index)
            new_index = (num_index + num[0] + len(nums)) % len(nums)
            nums.insert(new_index, num)

    ans = 0
    zero_index = nums.index(zero_obj)
    for j in range(1000,3001,1000):
        ans += nums[((zero_index + j)%len(nums))][0]
    return ans

print("Part 1:",solve())
print("Part 2:",solve(811589153,10))