
def problem3(slopes):
    f = open("/home/ec2-user/environment/AOC/Resources/problem3.txt")
    current = f.readline().strip()
    #skip line 1, start at index 3 on line 2
    if current is not None:
        current = f.readline().strip()
    linesize = len(current)
    
    # list of the amount to increment each line per slope
    indexCounter = slopes
    # loop counter, loop begins on the second line so begin at the indexCounter value
    currentIndex = []
    trees = []
    for z in range(len(slopes)):
        trees.append(0)
        currentIndex.append(indexCounter[z])
    
    while(current is not None and current != ""):
        for i in range(len(currentIndex)):
            # check if current index is an int, for the case of a 0.5 slope (only check trees on every other line)
            if currentIndex[i] == int(currentIndex[i]):
                if current[int(currentIndex[i])] == '#':
                    trees[i] += 1
            
            # increment current x-index per slope, wrapping around if out of index range
            currentIndex[i] = (currentIndex[i] + indexCounter[i]) % linesize
        
        current = f.readline().strip()
    
    returnval = trees[0]
    if len(trees) > 1:
        for j in trees[1:]:
            returnval *= j
    return returnval

print(problem3([3]))
print(problem3([1, 3, 5, 7, 0.5]))