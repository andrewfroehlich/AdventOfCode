import re

def build_sensors():
    sensors = []
    for line in open("input15.txt").read().splitlines():
        s_x,s_y,b_x,b_y = tuple(map(int, re.findall(r"\-?\d+", line)))
        sensors.append( (s_x,s_y,b_x,b_y,(abs(s_x - b_x) + abs(s_y - b_y))) )
    return sensors

def part1(y):
    no_beacon_x = set() #only for y argument
    beacon_x = set() #only for y argument
    sensors = build_sensors()
    for s_x,s_y,b_x,b_y,dist in sensors:
        if b_y == y:
            beacon_x.add( b_x )
        dist_remaining = dist - abs(y - s_y)
        if dist_remaining >= 0:
            for i in range(dist_remaining+1):
                no_beacon_x.add( s_x+i )
                no_beacon_x.add( s_x-i )
    return len(no_beacon_x - beacon_x)

def sensors_cover(sensors,target_x,target_y,min_c,max_c):
    if not (min_c <= target_x <= max_c and min_c <= target_y <= max_c):
        return True
    for s_x,s_y,_,_,dist in sensors:
        if (abs(s_x - target_x) + abs(s_y - target_y)) <= dist:
            return True
    return False

def part2b(min_c,max_c):
    sensors = build_sensors()
    for sensor_i in range(len(sensors)):
        s_x,s_y,_,_,dist = sensors[sensor_i]
        # check the full perimeter around the outside, start at the top
        cur_x,cur_y = s_x,s_y+dist+1
        while cur_y > s_y:
            if not sensors_cover(sensors,cur_x,cur_y,min_c,max_c):
                return cur_x*4000000 + cur_y
            cur_x,cur_y = cur_x+1,cur_y-1
        while cur_y > s_y-dist-1:
            if not sensors_cover(sensors,cur_x,cur_y,min_c,max_c):
                return cur_x*4000000 + cur_y
            cur_x,cur_y = cur_x-1,cur_y-1
        while cur_y < s_y:
            if not sensors_cover(sensors,cur_x,cur_y,min_c,max_c):
                return cur_x*4000000 + cur_y
            cur_x,cur_y = cur_x-1,cur_y+1
        # for all points out of the range of this sensor by 1, check if it is covered by any other sensor
        while cur_y < s_y+dist+1:
            if not sensors_cover(sensors,cur_x,cur_y,min_c,max_c):
                return cur_x*4000000 + cur_y
            cur_x,cur_y = cur_x+1,cur_y+1
    return -1

print("Part 1:",part1(2000000))
print("Part 2:",part2b(0,4000000))