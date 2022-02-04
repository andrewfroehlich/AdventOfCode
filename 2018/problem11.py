from functools import lru_cache

def power_level(x,y):
    power = 0
    power = (7315 + (y * (10 + x) )) * (10 + x)
    power = power % 1000
    power = (power - (power%100))//100
    return power-5

power_levels = [[0 for _ in range(301)] for _ in range(301)]
for x in range(1,301):
    for y in range(1,301):
        power_levels[x][y] = power_level(x,y)
        
@lru_cache(maxsize=300000000)
def power_of_block(x,y,size):
    if size == 1:
        return power_levels[x][y]
    else:
        return (power_of_block(x,y,size-1) + 
            sum([power_levels[i][y+size-1] for i in range(x,x+size)]) +
            sum([power_levels[x+size-1][j] for j in range(y,y+size-1)]))

part1 = (-1,-1,0) #x,y,power
part2 = (-1,-1,0,0) #x,y,size,power
for size in range(1,300):
    for x in range(1, 301-size):
        for y in range(1, 301-size):
            block_power = power_of_block(x,y,size)
            if block_power > part2[-1]:
                part2 = (x,y,size,block_power)
            if size == 3 and block_power > part1[-1]:
                part1 = (x,y,block_power)

print("Part 1:","{},{}".format(part1[0],part1[1]))
print("Part 2:","{},{},{}".format(str(part2[0]),str(part2[1]),str(part2[2])))