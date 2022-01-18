from collections import defaultdict
from collections import deque

lines = open("Resources/input10.txt").readlines()
bots = defaultdict(list)
bot_instructions = dict()
output = dict()
ready_bots = deque()
for line in lines:
    if line[0:5] == "value":
        _,val,_,_,_,bot = line.strip().split()
        if bot in bots:
            ready_bots.append(bot)
        bots[bot].append(int(val))
    else:
        _,src,_,_,_,low_ob,low,_,_,_,high_ob,high = line.split()
        bot_instructions[src] = (low_ob,low,high_ob,high)

while ready_bots:
    current_bot = ready_bots.popleft()
    val1,val2 = bots[current_bot]
    if val1 in (17,61) and val2 in (17,61):
        print("Part 1:",current_bot)
    low_ob,low,high_ob,high = bot_instructions[current_bot]
    if low_ob == "bot":
        if low in bots:
            ready_bots.append(low)
        bots[low].append(min(val1,val2))
    else: #output
        output[low] = min(val1,val2)
    if high_ob == "bot":
        if high in bots:
            ready_bots.append(high)
        bots[high].append(max(val1,val2))
    else: #output
        output[high] = max(val1,val2)
print("Part 2:",output["0"]*output["1"]*output["2"])