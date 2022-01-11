import functools

def part1(p1_pos,p2_pos):
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

@functools.lru_cache(maxsize=None)
def part2(current_pos, other_pos, current_score, other_score):
    if current_score >= 21:
        return 1, 0
    if other_score >= 21:
        return 0, 1
    p1_wins = p2_wins = 0
    for rollsum, count in universesPerRoll:
        new_pos = (current_pos + rollsum - 1) % 10 + 1
        opp_wins, player_wins = part2(other_pos, new_pos, other_score, current_score + new_pos)

        p1_wins += player_wins * count
        p2_wins += opp_wins * count
    return p1_wins, p2_wins
    
p1_pos,p2_pos = [int(c[-1]) for c in open("input21.txt").read().strip().split('\n')]
print("Part 1:",part1(p1_pos,p2_pos))

#27 universe possibilities for 3 rolls of 1-3, this is the count of universes per sum
universesPerRoll = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]
wins = part2(p1_pos, p2_pos, 0, 0)
print("Part 2:",max(wins))