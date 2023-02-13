Hercules = {"Health": 100, "Attack Power": 5, "Attacks": ["Punch", "Kick", "Sword"], "Armor Class": 15}
Nemean_Lion = {"Health": 50, "Attack Power": 3, "Attacks": ["Claws", "Bite", "Pounce"], "Armor Class": 12}
Lernaean_Hydra = {"Health": 150, "Attack Power": 6, "Attacks": ["Multi-Bite", "Tail-Whip"], "Armor Class": 13}
Cerberus = {"Health": 200, "Attack Power": 8, "Attacks": ["Multi-Bite", "Pounce"], "Armor Class": 16 }

import random

def pick_random_value(list_of_values):
    selected_value = random.choice(list_of_values)
    return selected_value

def Attack(chosen_attack):
    attack_chance = chosen_attack + random.randint(1,20)
    print(attack_chance)
    return attack_chance

Attack(Hercules.get("Attack Power"))