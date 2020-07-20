
import random
import yaml

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


class Character:

    def __init__(self, name, number_of_attacks, hit_modifier, damage_modifier,
                damage_dice, critical_range):
        self.name = name
        self.number_of_attacks = number_of_attacks
        self.hit_modifier = hit_modifier
        self.damage_modifier = damage_modifier
        dice = damage_dice.split("d")
        self.damage_dice_count = dice[0]
        self.damage_dice_size = dice[1]
        self.critical_range = critical_range


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

sample_characters = []

with open("characters.yaml") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    for character in data:
        for name,stats in character.items():
            sample_characters.append(Character(
                name=name, 
                number_of_attacks=stats["number_of_attacks"],
                hit_modifier=stats["hit_modifier"],
                damage_modifier=stats["damage_modifier"],
                damage_dice=stats["damage_dice"],
                critical_range=stats["critical_range"]))


# for turn in range (20):
#     print(f"Attack Action...{do_turn()} damage done")
print(sample_characters)