import random
import yaml


class Character:
    """
    Character class for holding the details around the character
    This will be passed around and used by functions for calculating various
    dice rolls
    """
    def __init__(self, name, number_of_attacks, hit_modifier, damage_modifier,
                damage_dice, critical_range):
        self.name = name
        self.number_of_attacks = number_of_attacks
        self.hit_modifier = hit_modifier
        self.damage_modifier = damage_modifier
        dice = damage_dice.split("d")
        self.damage_dice_count = int(dice[0])
        self.damage_dice_size = int(dice[1])
        self.critical_range = critical_range



def roll_dice(number_of_dice, die_size):
    total = 0
    for i in range (number_of_dice):
        total += random.randint(1,die_size)
    return total

def do_attack(character):
    hit_mod = character.hit_modifier
    dmg_mod = character.damage_modifier
    target_ac = 11
    dmg_dice_size = character.damage_dice_size
    dmg_dice_count = character.damage_dice_count

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


def do_turn(character):
    num_attacks = character.number_of_attacks
    total_damage = 0

    for attack in range (num_attacks):
        total_damage += do_attack(character)
    
    return total_damage


def load_sample_characters():
    """
    Used to load the character data into a usable array of Character classes
    """
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
                    critical_range=stats["critical_range"]
                    )
                )
    return sample_characters

# for turn in range (20):
#     print(f"Attack Action...{do_turn()} damage done")
for character in load_sample_characters():
    print(do_turn(character))