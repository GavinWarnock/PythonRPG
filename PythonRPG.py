Hercules = {"Health": 50, "Attack Power": 5, "Attacks": ["Punch", "Kick", "Sword"], "Armor Class": 15}
Nemean_Lion = {"Health": 25, "Attack Power": 3, "Attacks": ["Claws", "Bite", "Pounce"], "Armor Class": 12}
Lernaean_Hydra = {"Health": 60, "Attack Power": 6, "Attacks": ["Multi-Bite", "Tail-Whip"], "Armor Class": 13}
Cerberus = {"Health": 80, "Attack Power": 8, "Attacks": ["Multi-Bite", "Pounce"], "Armor Class": 16 }

import random

def pick_random_value(list_of_values):
    selected_value = random.choice(list_of_values)
    return selected_value

def Attack(enemy):
    attack = input("Which attack would you like to use? Punch, Kick, or Sword ")
    if attack == "Punch":
        attack_chance = Hercules.get("Attack Power") + random.randint(1,20)
        print(f"Your attack roll is {attack_chance}")
        if attack_chance >= enemy:
            print("You have struck true!")
            Punch(Hercules.get("Attack Power"))
        else:
            print("Your attack missed!")     
    elif attack == "Kick":
        attack_chance = Hercules.get("Attack Power") + random.randint(1,20)
        print(f"Your attack roll is {attack_chance}")
        if attack_chance >= enemy:
            print("You have struck true!")
            Kick(Hercules.get("Attack Power"))
        else:
            print("Your attack missed!")
    elif attack == "Sword":
        attack_chance = Hercules.get("Attack Power") + random.randint(1,20)
        print(f"Your attack roll is {attack_chance}")
        if attack_chance >= enemy:
            print("You have struck true!")
            Sword(Hercules.get("Attack Power"))
        else:
            print("Your attack missed!")
    else:
        print("Please select an valid attack.")

    
            
        


def Sword(attack_power):
    damage_dealt = attack_power + random.randint(1,10)
    print(f"Your sword did {damage_dealt} damage!")

def  Punch(attack_power):
    damage_dealt = attack_power + random.randint(1,6)
    print(f"Your punch did {damage_dealt} damage!")
    return(damage_dealt)

def Kick(attack_power):
    damage_dealt = attack_power + random.randint(1,8)
    print(f"Your kick did {damage_dealt} damage!")
    return damage_dealt
Attack(Nemean_Lion.get("Armor Class"))
