
import random
from enum import Enum 

# Dice = Enum(
#     "d20"=20,
#     "d12"=12,
#     d10=10,
#     d8=8,
#     d6=6,
#     d4=4
# )

# fighter = {
#     "dmg_dice": Dice.d10
# }

NAT20=20
NAT1=1

DICE = {
    "d20":20,
    "d12":12,
    "d10":10,
    "d8":8,
    "d6":6,
    "d4":4
}

def roll_attack():
    mod = 7
    roll = roll_dice(1,20)
    return {
        roll:roll,
        mod:mod,
        total:roll + mod
    }

def roll_dice(num, die):
    value = 0
    for i in range (0,num):
        value += random.randint(1,die)
    return value

def does_hit(target_ac, roll):
    if roll.roll == NAT20: return true
    elif roll.roll == NAT1: return false
    elif roll.total >= target_ac: return true
    else: return false


def do_attack():
    hit_mod = 7
    dmg_mod = 4
    target_ac = 11
    dmg_dice_size = 6
    dmg_dice_count = 1

    # Roll Attack Dice
    roll = roll_dice(1,20)
    print(f"I rolled: {roll}")

    # Check if crit/fail
    is_crit, is_fail = False, False
    if roll == 20: 
        is_crit = True
        dmg_dice_count += dmg_dice_count
    elif roll == 1: return 0

    # Add Modifier
    total_roll = roll + hit_mod

    # Compare against target AC
    damage = 0
    if is_crit or total_roll >= target_ac:
        # Determine Damage
        damage += dmg_mod
        for i in range(dmg_dice_count):
            damage += roll_dice(1,dmg_dice_size)
    
    return damage

def do_turn():
    num_attacks = 3
    total_damage = 0

    for attack in range (num_attacks):
        total_damage += do_attack()
    
    return total_damage


for turn in range (20):
    print(f"Attack Action...{do_turn()} damage done")

