from collections import Counter

def hand_rank(part_num, cards):
    if part_num == 1:
        return "".join([str(v[1]) for v in Counter(cards).most_common(2)])
    else:
        c = Counter(cards)
        jokers = c.pop("J") if "J" in c else 0
        if not c:
            return "5" #if c is now empty, we only had Jokers
        most_common = [str(v[1]) for v in c.most_common(2)]
        most_common[0] = str(int(most_common[0])+jokers) if jokers else most_common[0]
        return "".join(most_common)

def solve(part_num):
    by_hand_type = {"5":[],"41":[],"32":[],"31":[],"22":[],"21":[],"11":[]}
    sort_order = "AKQJT98765432" if part_num == 1 else "AKQT98765432J"
    rank_counter = 0
    for line in open("input.txt"):
        cards,val = line.split()
        rank_str = hand_rank(part_num, cards)
        by_hand_type[rank_str].append( (cards,int(val)) )
        rank_counter += 1
    
    answer = 0
    for rank_str in ["5","41","32","31","22","21","11"]:
        for hand,val in sorted(by_hand_type[rank_str], key=lambda word: [sort_order.index(c) for c in word[0]]):
            answer += rank_counter * val
            rank_counter -= 1
    return answer
    
if __name__ == "__main__":
    print("Part 1:",solve(1))
    print("Part 2:",solve(2))