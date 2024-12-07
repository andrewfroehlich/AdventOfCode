def list_safe(report):
    diff = 0
    for i in range(0,len(report)-1):
        new_diff = report[i+1]-report[i]
        if abs(new_diff) > 3 or new_diff == 0 or (diff * new_diff) < 0:
            return False
        diff = new_diff
    return True

def list_part2_safe(report):
    for i in range(len(report)):
        if list_safe(report[:i] + report[i+1:]):
            return True
    return False

def run(is_part2):
    ans = 0
    for line in open("input.txt"):
        report = [int(d) for d in line.split()]
        if list_safe(report):
            ans += 1
        elif is_part2:
            ans += 1 if list_part2_safe(report) else 0
    return ans

if __name__ == "__main__":
    print("Part 1:",run(False))
    print("Part 2:",run(True))