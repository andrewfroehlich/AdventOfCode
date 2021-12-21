def part1():
    p1_pos,p2_pos = [int(c[-1]) for c in open("input21.txt").read().strip().split('\n')]
    p1_score = p2_score = 0
    rolls = 0 
    while True:
        totalroll = (((rolls)%100)+1) + (((rolls+1)%100)+1) + (((rolls+2)%100)+1)
        if rolls % 6 < 3:
            p1_pos = ((p1_pos-1 + totalroll) % 10) + 1
            p1_score += p1_pos
        else:
            p2_pos = ((p2_pos-1 + totalroll) % 10) + 1
            p2_score += p2_pos
        rolls += 3
        if p1_score >= 1000:
            return rolls * p2_score
        elif p2_score >= 1000:
            return rolls * p1_score

print("Part 1:",part1())