
def part1():
    f = open("/home/ec2-user/environment/AOC/Resources/problem1.txt")
    s = set()
    current = f.readline().strip()
    currentInt = 0
    answer = 0
    while(current is not None):
        currentInt = int(current)
        if((2020 - currentInt) not in s):
            s.add(currentInt)
        else:
            return currentInt * (2020-currentInt)
        current = f.readline().strip()
        
print(part1())

def part2():
    f = open("/home/ec2-user/environment/AOC/Resources/problem1.txt")
    s = set()
    values = []
    current = f.readline().strip()
    while(current is not None and current != ""):
        s.add(int(current))
        values.append(int(current))
        current = f.readline().strip()
    
    for i in range(len(values)):
        for j in range(len(values)):
            if(i != j and (2020 - values[i] - values[j]) in s):
                return values[i] * values[j] * (2020 - values[i] - values[j])

print(part2())
                
        