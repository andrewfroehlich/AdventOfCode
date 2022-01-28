from collections import defaultdict

no_overlap = set()
part1 = 0
coord_to_claim = defaultdict(list)
for line in open("Resources/input3.txt"):
    num,_,corner,dimensions = line.strip().split()
    claim_id = num[1:]
    x,y = [int(a) for a in corner.replace(":","").split(",")]
    l,h = [int(b) for b in dimensions.split("x")]
    found_overlap = False
    for i in range(x, x+l):
        for j in range(y, y+h):
            coord_to_claim[(i,j)].append(claim_id)
            if len(coord_to_claim[(i,j)]) > 1:
                found_overlap = True
                if len(coord_to_claim[(i,j)]) == 2:
                    part1 += 1
                    no_overlap.discard(coord_to_claim[(i,j)][0])
    if not found_overlap:
        no_overlap.add(claim_id)
print("Part 1:",part1,"\nPart 2:",list(no_overlap)[0])