
def part1():
    f = open("/home/ec2-user/environment/AOC/Resources/problem2.txt")
    current = f.readline().strip()
    valid = 0
    while(current is not None and current != ""):
        
        curSplit = current.split()
        if(len(curSplit) != 3):
            raise Exception("Input not as expected: "+current)
        
        # first section, example "1-9"
        nums = curSplit[0].split("-")
        low = int(nums[0])
        high = int(nums[1])
        
        # second section, example "b:"
        char = (curSplit[1])[0]
        
        # third section, password, example "abcdef"
        occurances = curSplit[2].count(char)
        if(occurances >= low and occurances <= high):
            valid += 1
        
        current = f.readline().strip()
    
    return valid
    
    

print(part1())

def part2():
    f = open("/home/ec2-user/environment/AOC/Resources/problem2.txt")
    current = f.readline().strip()
    valid = 0
    while(current is not None and current != ""):
        
        curSplit = current.split()
        if(len(curSplit) != 3):
            raise Exception("Input not as expected: "+current)
        
        # first section, example "1-9"
        nums = curSplit[0].split("-")
        pos1 = int(nums[0])-1
        pos2 = int(nums[1])-1
        
        # second section, example "b:"
        char = (curSplit[1])[0]
        
        # third section, password, example "abcdef"
        occurances = 0
        if((curSplit[2])[pos1] == char):
            occurances += 1
        if((curSplit[2])[pos2] == char):
            occurances += 1
        
        if(occurances == 1):
            valid += 1
        
        current = f.readline().strip()
    
    return valid

print(part2())