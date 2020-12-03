
def part1():
    f = open("/home/ec2-user/environment/AOC/Resources/problem3.txt")
    current = f.readline().strip()
    #skip line 1, start at index 3 on line 2
    if current is not None:
        current = f.readline().strip()
    linesize = len(current)
    index = 3
    trees = 0
    
    while(current is not None and current != ""):
        
        if(current[index] == "#"):
            trees += 1
        
        
        # increment line and index
        current = f.readline().strip()
        index += 3
        if(index >= linesize):
            index -= linesize
    
    return trees
    
    

print(part1())

def part2():
    f = open("/home/ec2-user/environment/AOC/Resources/problem3.txt")
    current = f.readline().strip()
    #skip line 1, start at index 3 on line 2
    if current is not None:
        current = f.readline().strip()
    linesize = len(current)
    
    # 0 - Right 1, down 1.
    # 1 - Right 3, down 1.
    # 2 - Right 5, down 1.
    # 3 - Right 7, down 1.
    # 4 - Right 1, down 2.
    indexCounter = [1, 3, 5, 7, 0.5]
    currentIndex = [1, 3, 5, 7, 0.5]
    trees = [0, 0, 0, 0, 0]
    
    while(current is not None and current != ""):
        
        for i in range(len(currentIndex)):
            if currentIndex[i] == int(currentIndex[i]):
                if current[int(currentIndex[i])] == '#':
                    trees[i] += 1
            
            currentIndex[i] += indexCounter[i]
            if currentIndex[i] >= linesize:
                currentIndex[i] -= linesize
        
        current = f.readline().strip()
    
    returnval = 1
    for j in trees:
        returnval *= j
    return returnval

print(part2())