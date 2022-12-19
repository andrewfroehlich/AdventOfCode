import re
from collections import deque

def max_geodes(steps,ore_ore,clay_ore,obs_ore,obs_clay,geo_ore,geo_obs):
    dfs = deque( [(0,0,1,0,0,0,0,0,0)] ) #step, ore, ore robot, clay, clay robot, obs, obs robot, geode, geode robot
    visited = set( [(0,0,1,0,0,0,0,0,0)] )
    max_ore_robots = max(clay_ore,obs_ore,geo_ore) #you never need more ore robots than the max ore required to build
    maxg = 0
    while dfs:
        step,ore,oreR,clay,clayR,obs,obsR,geo,geoR = dfs.pop()
        maxg = max(maxg, geo)
        if step < steps:
            possible_max_g = geo + (steps-step)*geoR
            if (steps-step-1) > 0:
                possible_max_g += ((steps-step-1)*(steps-step))//2
            # add all possible robot actions including wait
            if possible_max_g > maxg:
                # build geode robot
                if ore >= geo_ore and obs >= geo_obs and (step+1,ore-geo_ore+oreR,oreR,clay+clayR,clayR,obs-geo_obs+obsR,obsR,geo+geoR,geoR+1) not in visited:
                    visited.add( (step+1,ore-geo_ore+oreR,oreR,clay+clayR,clayR,obs-geo_obs+obsR,obsR,geo+geoR,geoR+1) )
                    dfs.append( (step+1,ore-geo_ore+oreR,oreR,clay+clayR,clayR,obs-geo_obs+obsR,obsR,geo+geoR,geoR+1) )
                # build obs robot
                if obsR < geo_obs and ore >= obs_ore and clay >= obs_clay and (step+1,ore-obs_ore+oreR,oreR,clay-obs_clay+clayR,clayR,obs+obsR,obsR+1,geo+geoR,geoR) not in visited:
                    visited.add( (step+1,ore-obs_ore+oreR,oreR,clay-obs_clay+clayR,clayR,obs+obsR,obsR+1,geo+geoR,geoR) )
                    dfs.append( (step+1,ore-obs_ore+oreR,oreR,clay-obs_clay+clayR,clayR,obs+obsR,obsR+1,geo+geoR,geoR) )
                #wait
                if (step+1,ore+oreR,oreR,clay+clayR,clayR,obs+obsR,obsR,geo+geoR,geoR) not in visited:
                    visited.add( (step+1,ore+oreR,oreR,clay+clayR,clayR,obs+obsR,obsR,geo+geoR,geoR) )
                    dfs.append( (step+1,ore+oreR,oreR,clay+clayR,clayR,obs+obsR,obsR,geo+geoR,geoR) )
                # build ore robot
                if oreR < max_ore_robots and ore >= ore_ore and (step+1,ore-ore_ore+oreR,oreR+1,clay+clayR,clayR,obs+obsR,obsR,geo+geoR,geoR) not in visited:
                    visited.add( (step+1,ore-ore_ore+oreR,oreR+1,clay+clayR,clayR,obs+obsR,obsR,geo+geoR,geoR) )
                    dfs.append( (step+1,ore-ore_ore+oreR,oreR+1,clay+clayR,clayR,obs+obsR,obsR,geo+geoR,geoR) )
                # build clay robot
                if clayR < obs_clay and ore >= clay_ore and (step+1,ore-clay_ore+oreR,oreR,clay+clayR,clayR+1,obs+obsR,obsR,geo+geoR,geoR) not in visited:
                    visited.add( (step+1,ore-clay_ore+oreR,oreR,clay+clayR,clayR+1,obs+obsR,obsR,geo+geoR,geoR) )
                    dfs.append( (step+1,ore-clay_ore+oreR,oreR,clay+clayR,clayR+1,obs+obsR,obsR,geo+geoR,geoR) )
    return maxg

def part1(file):
    part1 = 0
    for line in open(file).read().splitlines():
        num,ore_ore,clay_ore,obs_ore,obs_clay,geo_ore,geo_obs = tuple(map(int, re.findall(r"\d+", line)))
        part1 += num * max_geodes(24,ore_ore,clay_ore,obs_ore,obs_clay,geo_ore,geo_obs)
    return part1

def part2(file):
    part2 = 1
    lines = open(file).read().splitlines()
    for i in range(3):  
        num,ore_ore,clay_ore,obs_ore,obs_clay,geo_ore,geo_obs = tuple(map(int, re.findall(r"\d+", lines[i])))
        part2 = part2 * max_geodes(32,ore_ore,clay_ore,obs_ore,obs_clay,geo_ore,geo_obs)
    return part2

print("Part 1:",part1("input19.txt"))
print("Part 2:",part2("input19.txt"))