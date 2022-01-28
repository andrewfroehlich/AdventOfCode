from collections import defaultdict

lines = open("Resources/input4.txt").readlines()
lines.sort()
line_index = 0
guards = dict()
totals = defaultdict(int)
most_asleep_guard = (-1,-1) #(id, minutes asleep)
while line_index < len(lines):
    guard_id = int(lines[line_index].split()[3][1:])
    if guard_id not in guards:
        guards[guard_id] = defaultdict(int)
    line_index += 1
    while line_index < len(lines) and "Guard" not in lines[line_index]:
        asleep_time = int(lines[line_index].split()[1][3:5])
        awake_time = int(lines[line_index+1].split()[1][3:5])
        for t in range(asleep_time,awake_time):
            guards[guard_id][t] += 1
        totals[guard_id] += awake_time-asleep_time
        if totals[guard_id] > most_asleep_guard[1]:
            most_asleep_guard = (guard_id, totals[guard_id])
        line_index += 2

most_asleep_minute = (-1,-1) #(minute, total asleep)
for minute in guards[most_asleep_guard[0]]:
    if guards[most_asleep_guard[0]][minute] > most_asleep_minute[1]:
        most_asleep_minute = (minute, guards[most_asleep_guard[0]][minute])
print("Part 1:", most_asleep_guard[0]*most_asleep_minute[0])

most_asleep_minute = (-1,-1,-1) #(minute, total asleep, guard_id)
for guard_id in guards:
    for minute in guards[guard_id]:
        if guards[guard_id][minute] > most_asleep_minute[0]:
            most_asleep_minute = (minute, guards[guard_id][minute], guard_id)
print("Part 2:", most_asleep_minute[0]*most_asleep_minute[2])