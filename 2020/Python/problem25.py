public_keys = [int(d) for d in open("../Resources/problem25.txt").read().splitlines()]
val,loop = 1,0
while val not in public_keys:
    loop += 1
    val = (val * 7)%20201227
subject = public_keys[0] if val==public_keys[1] else public_keys[1]
val = 1
for i in range(loop):
    val = (val * subject)%20201227
print("Part 1:",val)