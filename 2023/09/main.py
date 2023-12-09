def difference_list(input_list):
    diff = []
    for i in range(len(input_list)-1):
        diff.append(input_list[i+1]-input_list[i])
    return diff

def solve():
    sum1 = sum2 = 0
    for line in open("input.txt"):
        last_nums,first_nums = [],[]
        current = [int(d) for d in line.split()]
        while not all(v == 0 for v in current):
            last_nums.append(current[-1])
            first_nums.append(current[0])
            current = difference_list(current)
        sum1 += sum(last_nums)
        current = 0
        for i in range(len(first_nums)-1,-1,-1):
            current = first_nums[i] - current
        sum2 += current
    return sum1,sum2

if __name__ == "__main__":
    p1,p2 = solve()
    print("Part 1:",p1)
    print("Part 2:",p2)