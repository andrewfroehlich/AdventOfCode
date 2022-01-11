def solveDigits(digits):
    digitMap = dict()
    
    #find 2, 3, 4, 7 first, to use segment info to aid in the rest
    remainingDigits = []
    cf = "" #the C+F segment is helpful in determining the remaining digits
    digit4 = ""
    for digit in digits:
        digit = ''.join(sorted(digit))
        if len(digit) == 2:
            digitMap[digit] = 1
            cf = digit
        elif len(digit) == 3:
            digitMap[digit] = 7
        elif len(digit) == 4:
            digitMap[digit] = 4
            digit4 = digit
        elif len(digit) == 7:
            digitMap[digit] = 8
        else:
            remainingDigits.append(digit)
    digits = remainingDigits
    bd = digit4.replace(cf[0],'').replace(cf[1],'') #as is the B+D segment
    
    # find all the rest
    for digit in digits:
        digit = ''.join(sorted(digit))
        if len(digit)==5 and cf[0] in digit and cf[1] in digit:
            digitMap[digit] = 3
        elif len(digit)==5 and bd[0] in digit and bd[1] in digit:
            digitMap[digit] = 5
        elif len(digit)==5:
            digitMap[digit] = 2
        elif len(digit)==6 and (not cf[0] in digit or not cf[1] in digit):
            digitMap[digit] = 6
        elif len(digit)==6 and bd[0] in digit and bd[1] in digit:
            digitMap[digit] = 9
        else:
            digitMap[digit] = 0
    return digitMap

def getValue(digitMap, digits):
    ret = 0
    multiplier = 1000
    for digit in digits:
        digit = ''.join(sorted(digit))
        ret += int(digitMap.get(digit)) * multiplier
        multiplier = multiplier / 10
    return int(ret)

def part1():
    f = open("input8.txt")
    answer = 0
    for line in f:
        output = (line.split(" | ")[1]).split()
        for digit in output:
            if len(digit) in [2,3,4,7]:
                answer += 1
    return answer

def part2():
    f = open("input8.txt")
    answer = 0
    for line in f:
        parseLine = line.split(" | ")
        digitMap = solveDigits(parseLine[0].split())
        answer += getValue(digitMap, parseLine[1].split())
    return answer

print("Part 1:",part1())
print("Part 2:",part2())