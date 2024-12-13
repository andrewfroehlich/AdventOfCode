def is_int(value, tolerance=1e-3):
    return abs(value - round(value)) < tolerance

def run(adjustment):
    tokens,i = 0,0
    lines = open("input.txt").read().splitlines()
    while i < len(lines):
        z,y = [int(d) for d in lines[i][len("Button A: X+"):].split(", Y+")]
        x,w = [int(d) for d in lines[i+1][len("Button B: X+"):].split(", Y+")]
        v,u = [int(d)+adjustment for d in lines[i+2][len("Prize: X="):].split(", Y=")]
        b = (u - (y*v/z)) / (w - (x*y)/z)
        a = (v - x*b) / z
        if is_int(a) and is_int(b):
            tokens += round(3*a + b)
        i += 4
    return tokens

if __name__ == "__main__":
    print("Part 1:",run(0))
    print("Part 2:",run(10000000000000))