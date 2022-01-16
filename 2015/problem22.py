import sys

boss_hp = 71
boss_dmg = 10
spells = {
    "Missile":{"mana":53,"damage":4},
    "Drain":{"mana":73,"damage":2,"heal":2},
    "Shield":{"mana":113,"duration":6,"armor":7},
    "Poison":{"mana":173,"duration":6,"dot":3},
    "Recharge":{"mana":229,"duration":5,"mana_heal":101}
}
my_hp = 50
my_mana = 500

def turn(next_spell,mana_spent,my_mana,my_hp,boss_hp,shield_left,poison_left,recharge_left,hard_mode):
    global min_found
    
    if hard_mode:
        my_hp -= 1
        if my_hp <= 0:
            return sys.maxsize
    
    #process effects over time
    if shield_left > 0:
        shield_left -= 1
    if poison_left > 0:
        boss_hp -= spells["Poison"]["dot"]
        if boss_hp <= 0:
            min_found = min(min_found,mana_spent)
            return mana_spent
        poison_left -= 1
    if recharge_left > 0:
        my_mana += spells["Recharge"]["mana_heal"]
        recharge_left -= 1
    
    #process next_spell
    my_mana -= spells[next_spell]["mana"]
    mana_spent += spells[next_spell]["mana"]
    if my_mana < 0 or mana_spent > min_found:
        return sys.maxsize
    if next_spell == "Shield":
        if shield_left > 0:
            return sys.maxsize
        else:
            shield_left = spells[next_spell]["duration"]
    elif next_spell == "Recharge":
        if recharge_left > 0:
            return sys.maxsize
        else:
            recharge_left = spells[next_spell]["duration"]
    elif next_spell == "Poison":
        if poison_left > 0:
            return sys.maxsize
        else:
            poison_left = spells[next_spell]["duration"]
    if "heal" in spells[next_spell]:
        my_hp += spells[next_spell]["heal"]
    if "damage" in spells[next_spell]:
        boss_hp -= spells[next_spell]["damage"]
        if boss_hp <= 0:
            min_found = min(min_found,mana_spent)
            return mana_spent
    
    #process boss turn
    my_armor = 0
    if shield_left>0:
        my_armor = spells["Shield"]["armor"]
        shield_left -= 1
    if poison_left > 0:
        boss_hp -= spells["Poison"]["dot"]
        if boss_hp <= 0:
            min_found = min(min_found,mana_spent)
            return mana_spent
        poison_left -= 1
    if recharge_left > 0:
        my_mana += spells["Recharge"]["mana_heal"]
        recharge_left -= 1
    my_hp -= (boss_dmg - my_armor)
    if my_hp <= 0:
        return sys.maxsize
    
    #take next turn
    return min(turn("Recharge",mana_spent,my_mana,my_hp,boss_hp,shield_left,poison_left,recharge_left,hard_mode),
        turn("Poison",mana_spent,my_mana,my_hp,boss_hp,shield_left,poison_left,recharge_left,hard_mode),
        turn("Missile",mana_spent,my_mana,my_hp,boss_hp,shield_left,poison_left,recharge_left,hard_mode),
        turn("Shield",mana_spent,my_mana,my_hp,boss_hp,shield_left,poison_left,recharge_left,hard_mode),
        turn("Drain",mana_spent,my_mana,my_hp,boss_hp,shield_left,poison_left,recharge_left,hard_mode))

min_found = sys.maxsize
part1 = min(turn("Recharge",0,my_mana,my_hp,boss_hp,0,0,0,False),
        turn("Poison",0,my_mana,my_hp,boss_hp,0,0,0,False),
        turn("Missile",0,my_mana,my_hp,boss_hp,0,0,0,False),
        turn("Shield",0,my_mana,my_hp,boss_hp,0,0,0,False),
        turn("Drain",0,my_mana,my_hp,boss_hp,0,0,0,False))
print("Part 1:",part1)
min_found = sys.maxsize
part2 = min(turn("Recharge",0,my_mana,my_hp,boss_hp,0,0,0,True),
        turn("Poison",0,my_mana,my_hp,boss_hp,0,0,0,True),
        turn("Missile",0,my_mana,my_hp,boss_hp,0,0,0,True),
        turn("Shield",0,my_mana,my_hp,boss_hp,0,0,0,True),
        turn("Drain",0,my_mana,my_hp,boss_hp,0,0,0,True))
print("Part 2:",part2)