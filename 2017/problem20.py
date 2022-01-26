lines = open("Resources/input20.txt").readlines()
acc,vel,pos = dict(),dict(),dict()
min_accel_p = min_accel_abs = -1
for p_num in range(len(lines)):
    pos_raw,vel_raw,acc_raw = lines[p_num].strip().split(">, ")
    pos[p_num] = tuple([int(d) for d in pos_raw.split("=<")[1].split(",")])
    vel[p_num] = tuple([int(d) for d in vel_raw.split("=<")[1].split(",")])
    acc[p_num] = tuple([int(d) for d in acc_raw.split("=<")[1].strip(">").split(",")])
    a_dist = (abs(acc[p_num][0])+abs(acc[p_num][1])+abs(acc[p_num][2]))
    if min_accel_p == -1 or a_dist < min_accel_abs:
        min_accel_p = p_num
        min_accel_abs = a_dist
print("Part 1:",min_accel_p)

destroyed = set()
for steps in range(200):
    current_positions = dict()
    for p_num in range(len(lines)):
        if p_num in destroyed:
            continue
        ax,ay,az = acc[p_num]
        vx,vy,vz = vel[p_num]
        px,py,pz = pos[p_num]
        vx,vy,vz = vx+ax, vy+ay, vz+az
        px,py,pz = px+vx, py+vy, pz+vz
        vel[p_num] = (vx,vy,vz)
        pos[p_num] = (px,py,pz)
        if (px,py,pz) in current_positions:
            destroyed.add(p_num)
            destroyed.add(current_positions[(px,py,pz)])
        current_positions[(px,py,pz)] = p_num
print("Part 2:",len(lines) - len(destroyed))
