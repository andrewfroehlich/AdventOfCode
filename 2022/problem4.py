part1,part2 = 0,0
for line in open("input4.txt"):
    split1 = line.strip().split(",")
    low1,high1 = [int(d) for d in split1[0].split("-")]
    low2,high2 = [int(d) for d in split1[1].split("-")]
    if (low1 >= low2 and high1 <= high2) or (low2 >= low1 and high2 <= high1):
        part1 += 1
    if low1 <= low2 <= high1 or low1 <= high2 <= high1 or low2 <= low1 <= high2 or low2 <= high1 <= high2:
        part2 += 1
print("Part 1:",part1,"\nPart 2:",part2)