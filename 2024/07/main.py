from collections import deque

def evaluate(value,nums,is_part2):
    original_value = value
    queue = deque()
    queue.append( (value, tuple(nums)) )
    while queue:
        value,nums = queue.popleft()
        current = nums[-1]
        nums = nums[0:-1]
        if len(nums) == 0:
            if current == value:
                return original_value
        else:
            if value - current > 0:
                queue.append( (value-current, nums) )
            if value % current == 0:
                queue.append( (value//current, nums) )
            if is_part2 and value>current and str(value).endswith(str(current)):
                queue.append( (int(str(value)[0:0-(len(str(current)))]), nums) )
    return 0

def run(is_part2):
    ans = 0
    for line in open("input.txt"):
        value,equation = line.split(": ")
        nums = [int(d) for d in equation.split()]
        ans += evaluate(int(value),nums,is_part2)
    return ans

if __name__ == "__main__":
    print("Part 1:",run(False))
    print("Part 2:",run(True))