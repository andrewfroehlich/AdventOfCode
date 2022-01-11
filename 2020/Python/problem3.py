
def problem3(slopes):
    f = open("../Resources/problem3.txt")

    #skip line 1, tree counting begins on line 2
    current = f.readline().strip()
    linesize = len(current)
    
    # list of the amount to increment each line per slope
    indexCounter = slopes
    # loop counter, loop begins on the second line so begin each at the indexCounter value
    currentIndex = []
    trees = []
    for z in range(len(slopes)):
        trees.append(0)
        currentIndex.append(indexCounter[z])
    
    for current in f.readlines():
        for i in range(len(currentIndex)):
            # check if current index is an int for the 0.5 slope case (only check trees on every other line)
            if currentIndex[i] == int(currentIndex[i]):
                if current[int(currentIndex[i])] == '#':
                    trees[i] += 1
            
            # increment current x-index per slope, wrapping around if out of index range
            currentIndex[i] = (currentIndex[i] + indexCounter[i]) % linesize
        
    returnval = trees[0]
    if len(trees) > 1:
        for j in trees[1:]:
            returnval *= j
    return returnval

print(problem3([3]))
print(problem3([1, 3, 5, 7, 0.5]))