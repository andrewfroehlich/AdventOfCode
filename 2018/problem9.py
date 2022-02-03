def play(players, final_marble):
    marbles = [0]
    scores = [0]*players
    cur_i = pl_i = 0
    for mar in range(1, final_marble+1):
        if mar % 23 != 0:
            cur_i = (cur_i + 2) % len(marbles)
            marbles.insert(cur_i, mar)
        else:
            cur_i = (len(marbles) + cur_i - 7) % len(marbles)
            scores[pl_i] += mar + marbles.pop(cur_i)
        pl_i = (pl_i + 1)%players
        if mar % 100000 == 0:
            print("Marble",mar)
    return max(scores)

raw_input = open("Resources/input9.txt").readline().split()
players,final_marble = int(raw_input[0]), int(raw_input[6])
print("Part 1:", play(players,final_marble))
print("Part 2:", play(players,final_marble*100))