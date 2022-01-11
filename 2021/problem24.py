import itertools as it

# A is x addend, B is y addend, C is z divisor
As = [13,13,10,15,-8,-10,11,-3,14,-4,14,-5,-8,-11]
Bs = [15,16, 4,14, 1,  5, 1, 3, 3, 7, 5,13, 3, 10]
Cs = [ 1, 1, 1, 1,26, 26, 1,26, 1,26, 1,26,26, 26]

def solve(highest):
    zs = {0}
    result = {}
    if highest:
        ws = range(1,10)
    else:
        ws = range(9,0,-1)
    for A,B,C in zip(As[::-1],Bs[::-1],Cs[::-1]):
        newzs = set()
        for w,z in it.product(ws,zs):
            z0s = []
            x = z - w - B
            if x % 26 == 0:
                z0s.append(x//26 * C)
            if 0 <= w-A < 26:
                z0 = z * C
                z0s.append(w-A+z0)
            
            for z0 in z0s:
                newzs.add(z0)
                result[z0] = (w,) + result.get(z, ())
        zs = newzs
    return ''.join(str(digit) for digit in result[0])

print("Part 1:",solve(True))
print("Part 2:",solve(False))