vels,durs,rests,current,points = [],[],[],[],[]
for line in open("Resources/input14.txt"):
    _,_,_,vel,_,_,dur,*_,rest,_ = line.split()
    vels.append(int(vel))
    durs.append(int(dur))
    rests.append(int(rest))
    current.append(0)
    points.append(0)

for time in range(1,2504):
    current_lead = -1
    current_lead_i = []
    for i in range(len(vels)):
        if time % int(durs[i] + rests[i]) > 0 and time % int(durs[i] + rests[i]) <= durs[i]:
            current[i] += vels[i]
        if current[i] == current_lead:
            current_lead_i.append(i)
        elif current[i] > current_lead:
            current_lead = current[i]
            current_lead_i = [i]
    for i in current_lead_i:
        points[i] += 1

print("Part 1:",max(current),"\nPart 2:",max(points))