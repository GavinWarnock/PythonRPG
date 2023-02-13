Hercules = {"Health": 100, "Attack Power": 5, "Attacks": ["Punch", "Kick", "Sword"], "Armor Class": 15}
Nemean_Lion = {"Health": 25, "Attack Power": 3, "Attacks": ["Claws", "Multi-Bite", "Pounce"], "Armor Class": 12}
Lernaean_Hydra = {"Health": 60, "Attack Power": 6, "Attacks": ["Multi-Bite", "Tail-Whip"], "Armor Class": 13}
Cerberus = {"Health": 80, "Attack Power": 8, "Attacks": ["Multi-Bite", "Pounce"], "Armor Class": 16 }

import random

def pick_random_attack(list_of_attacks):                # Random attack funtion for enemy attacks
    selected_attack = random.choice(list_of_attacks)
    return selected_attack

def Sword(attack_power):
    damage_dealt = attack_power + random.randint(1,10)  # Different functions for Herc's attacks
    print(f"Your sword did {damage_dealt} damage!")
    return damage_dealt
def  Punch(attack_power):
    damage_dealt = attack_power + random.randint(1,6)
    print(f"Your punch did {damage_dealt} damage!")
    return(damage_dealt)
def Kick(attack_power):
    damage_dealt = attack_power + random.randint(1,8)
    print(f"Your kick did {damage_dealt} damage!")
    return damage_dealt

def Claws(attack_power):
    damage_dealt = attack_power + random.randint(1,6)
    print(f"The monsters claws rend your flesh for {damage_dealt} damage!")
    return damage_dealt
def Multi_Bite(attack_power):
    damage_dealt = attack_power + random.randint(1,8)
    print(f"The beast's fangs clench down for {damage_dealt} damage!")
    return damage_dealt
def Pounce(attack_power):
    damage_dealt = attack_power + random.randint(1,10)
    print(f"The beast rears back and pounces on you for {damage_dealt} damage!")
def Tail_Whip(attack_power):
    damage_dealt = attack_power + random.randint(1,12)
    print(f"The monster swipes it's mighty tail at you for {damage_dealt} damage!")


def Hercules_attack(enemy):
    attack = input("Which attack would you like to use? Punch, Kick, or Sword ")
    if attack == "Punch":
        attack_chance = Hercules.get("Attack Power") + random.randint(1,20)
        print(f"Your attack roll is {attack_chance}")
        if attack_chance >= enemy["Armor Class"]:
            print("You have struck true!")
            enemy["Health"] -= Punch(Hercules.get("Attack Power"))
        else:
            print("Your attack missed!")     
    elif attack == "Kick":
        attack_chance = Hercules.get("Attack Power") + random.randint(1,20)
        print(f"Your attack roll is {attack_chance}")
        if attack_chance >= enemy["Armor Class"]:
            print("You have struck true!")
            enemy["Health"] -= Kick(Hercules.get("Attack Power"))
        else:
            print("Your attack missed!")
    elif attack == "Sword":
        attack_chance = Hercules.get("Attack Power") + random.randint(1,20)
        print(f"Your attack roll is {attack_chance}")
        if attack_chance >= enemy["Armor Class"]:
            print("You have struck true!")
            enemy["Health"] -= Sword(Hercules.get("Attack Power"))

        else:
            print("Your attack missed!")
    else:
        print("Please select an valid attack.")

def Nemean_Lion_attack(Hercules):
    print("Your enemy readies a vicious blow!")
    foe_attack = pick_random_attack(Nemean_Lion["Attacks"])
    if foe_attack == "Claws":
        enemy_attack_chance = Nemean_Lion["Attack Power"] + random.randint(1,20)
        print(enemy_attack_chance)
        if enemy_attack_chance >= Hercules["Armor Class"]:
            print("You have been struck!")
            Hercules["Health"] -= Claws(Nemean_Lion["Attack Power"])
        else:
            print("The sweeping claw attack misses!")
    elif foe_attack == "Multi-Bite":
        enemy_attack_chance = Nemean_Lion["Attack Power"] + random.randint(1,20)
        print(enemy_attack_chance)
        if enemy_attack_chance >= Hercules["Armor Class"]:
            print("You have been struck!")
            Hercules["Health"] -= Multi_Bite(Nemean_Lion["Attack Power"])
        else:
            print("The lunging bite attack missed!")
    elif foe_attack == "Pounce":
        enemy_attack_chance = Nemean_Lion["Attack Power"] + random.randint(1,20)
        print(enemy_attack_chance)
        if enemy_attack_chance >= Hercules["Armor Class"]:
            print("You have been struck!")
            Hercules["Health"] -= Pounce(Nemean_Lion["Attack Power"])
        else:
            print("With a great leap the beast pounces and misses you!")
    else:
        print("Invalid Attack")

    
            


Hercules_attack(Nemean_Lion)
Nemean_Lion_attack(Hercules)