total = 0
for line in open("input25.txt").read().splitlines():
    current,five = 0,1
    for i in range(len(line)-1,-1,-1):
        current += five * (int(line[i]) if line[i].isnumeric() else (-2 if line[i]=="=" else -1))
        five = five * 5
    total += current

reverse_digits = []
while total > 0:
    if total % 5 == 3:
        reverse_digits.append("=")
        total += 2
    elif total % 5 == 4:
        reverse_digits.append("-")
        total += 1
    else:
        reverse_digits.append(str(total % 5))
    total = total // 5
reverse_digits.reverse()
print("Part 1:","".join(reverse_digits))