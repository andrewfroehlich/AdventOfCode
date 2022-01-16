import math

boss_hp = my_hp = 100
boss_dmg = 8
boss_arm = 2

#cost,dmg,arm
my_weapon = (0,0,0)
my_armor = (0,0,0)
my_ring1 = (0,0,0)
my_ring2 = (0,0,0)
weapons = [(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
armors = [(0,0,0),(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5)]
rings = [(0,0,0),(20,0,1),(25,1,0),(40,0,2),(50,2,0),(80,0,3),(100,3,0)]

lowest_cost_win = highest_cost_loss = -1
for my_weapon in weapons:
    for my_armor in armors:
        for my_ring1 in rings:
            for my_ring2 in rings:
                my_cost = my_weapon[0] + my_armor[0] + my_ring1[0] + my_ring2[0]
                my_dmg = my_weapon[1] + my_ring1[1] + my_ring2[1]
                my_arm = my_armor[2] + my_ring1[2] + my_ring2[2]
                
                turns_to_win = math.ceil(boss_hp / max((my_dmg - boss_arm),1))
                turns_to_lose = math.ceil(my_hp / max((boss_dmg - my_arm),1))
                if turns_to_win <= turns_to_lose and (lowest_cost_win == -1 or my_cost < lowest_cost_win):
                    lowest_cost_win = my_cost
                elif turns_to_win > turns_to_lose and my_cost > highest_cost_loss:
                    highest_cost_loss = my_cost
print("Part 1:",lowest_cost_win,"\nPart 2:",highest_cost_loss)