def first_highest_number(num_str,index1,index2):
    high_i = index1
    for i in range(index1+1,index2):
        if num_str[high_i] == "9":
            return high_i
        if num_str[i] > num_str[high_i]:
            high_i = i
    return high_i

def joltage(digits):
    part1 = 0
    for num_str in map(str.strip, open("input.txt")):
        current,last_i = [],-1
        for i in range(digits):
            last_i = first_highest_number(num_str,last_i+1,len(num_str) - (digits - 1 - i))
            current.append(num_str[last_i])
        part1 += int("".join(current))
    return part1

if __name__ == "__main__":
    print("Part 1:",joltage(2))
    print("Part 2:",joltage(12))