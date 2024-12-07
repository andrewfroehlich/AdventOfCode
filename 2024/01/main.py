from collections import Counter

def part1(list1,list2):
    part1 = 0
    for i in range(len(list1)):
        part1 += abs(list1[i] - list2[i])
    return part1

def part2(list1,list2):
    count = Counter(list2)
    part2 = 0
    for num in list1:
        part2 += (num * count[num])
    return part2

if __name__ == "__main__":
    list1,list2 = [],[]
    for line in open("input.txt"):
        num1,num2 = line.split("   ")
        list1.append(int(num1))
        list2.append(int(num2))
    list1.sort()
    list2.sort()
    print("Part 1:",part1(list1,list2))
    print("Part 2:",part2(list1,list2))