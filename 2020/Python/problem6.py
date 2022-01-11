
def part1():
    f = open("../Resources/problem6.txt")
    s = set()
    answer = 0
    for current in f.readlines():
        current = current.strip()
        if current == "\n" or current == "":
            s.clear()
        else:
            for c in current:
                if c not in s:
                    s.add(c)
                    answer += 1
    return answer
        
print(part1())

def part2():
    f = open("../Resources/problem6.txt")
    s = set()
    t = set()
    newgroup = True
    answer = 0
    for current in f.readlines():
        current = current.strip()
        if current == "\n" or current == "":
            answer += len(s)
            s.clear()
            newgroup = True
        else:
            # if this is the first line, fill the set
            if newgroup:
                newgroup = False
                for c in current:
                    s.add(c)
            else:
                for c in current:
                    t.add(c)
                s.intersection_update(t)
                t.clear()
    answer += len(s)
    return answer


print(part2()) 