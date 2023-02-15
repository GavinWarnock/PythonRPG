Hercules = {"Name": "Hercules", "Health": 100, "Attack Power": 5, "Attacks": ["Punch", "Kick", "Sword"], "Armor Class": 15}
Nemean_Lion = {"Name": "Nemean Lion", "Health": 25, "Attack Power": 3, "Attacks": ["Claws", "Multi-Bite", "Pounce"], "Armor Class": 12}
Lernaean_Hydra = {"Name": "Lernaean Hydra", "Health": 60, "Attack Power": 6, "Attacks": ["Multi-Bite", "Tail-Whip"], "Armor Class": 13}
Cerberus = {"Name": "Cerberus", "Health": 80, "Attack Power": 8, "Attacks": ["Multi-Bite", "Pounce"], "Armor Class": 16 }

import random

def pick_random_attack(list_of_attacks):                # Random attack funtion for enemy attacks
    selected_attack = random.choice(list_of_attacks)
    return selected_attack

def Sword(attack_power):
    damage_dealt = attack_power + random.randint(1,10)  # Different functions for Herc's attacks
    print(f"Your sword did {damage_dealt} damage!")
    return damage_dealt
def Punch(attack_power):
    damage_dealt = attack_power + random.randint(1,6)
    print(f"Your punch did {damage_dealt} damage!")
    return(damage_dealt)
def Kick(attack_power):
    damage_dealt = attack_power + random.randint(1,8)
    print(f"Your kick did {damage_dealt} damage!")
    return damage_dealt

def Claws(attack_power):
    damage_dealt = attack_power + random.randint(1,6)                # Different functions for enemy attacks
    print(f"The monsters claws rend your flesh for {damage_dealt} damage!")
    return damage_dealt
def Multi_Bite(attack_power):
    damage_dealt = attack_power + random.randint(1,8)
    print(f"The beast's fangs clench down for {damage_dealt} damage!")
    return damage_dealt
def Pounce(attack_power):
    damage_dealt = attack_power + random.randint(1,10)
    print(f"The beast rears back and pounces on you for {damage_dealt} damage!")
    return damage_dealt
def Tail_Whip(attack_power):
    damage_dealt = attack_power + random.randint(1,12)
    print(f"The monster swipes it's mighty tail at you for {damage_dealt} damage!")


def Hercules_attack(enemy):                                                 # Function for Herc's attacks against enemies
    attack = input("Which attack would you like to use? Punch, Kick, or Sword ")   # Function for Herc's attacks against enemies
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

def Nemean_Lion_attack(Hercules):                                           # Function for the Nemean Lion's attacks against Herc
    print("Your enemy readies a vicious blow!")
    foe_attack = pick_random_attack(Nemean_Lion["Attacks"])
    if foe_attack == "Claws":
        enemy_attack_chance = Nemean_Lion["Attack Power"] + random.randint(1,20)
        print(f"The beast attacks with a {enemy_attack_chance}")
        if enemy_attack_chance >= Hercules["Armor Class"]:
            print("You have been struck!")
            Hercules["Health"] -= Claws(Nemean_Lion["Attack Power"])
        else:
            print("The sweeping claw attack misses!")
    elif foe_attack == "Multi-Bite":
        enemy_attack_chance = Nemean_Lion["Attack Power"] + random.randint(1,20)
        print(f"The beast attacks with a {enemy_attack_chance}")
        if enemy_attack_chance >= Hercules["Armor Class"]:
            print("You have been struck!")
            Hercules["Health"] -= Multi_Bite(Nemean_Lion["Attack Power"])
        else:
            print("The lunging bite attack missed!")
    elif foe_attack == "Pounce":
        enemy_attack_chance = Nemean_Lion["Attack Power"] + random.randint(1,20)
        print(f"The beast attacks with a {enemy_attack_chance}")
        if enemy_attack_chance >= Hercules["Armor Class"]:
            print("You have been struck!")
            Hercules["Health"] -= Pounce(Nemean_Lion["Attack Power"])         # LINE BROKEN UNSURE AS TO WHY?
        else:
            print("With a great leap the beast pounces and misses you!")
    else:
        print("Invalid Attack")

def Lernaean_Hydra_attack(Hercules):                                        # Function for Lernaean Hydra's attacks against Herc
    print("Your enemy readies a vicious blow!")
    foe_attack = pick_random_attack(Lernaean_Hydra["Attacks"])
    if foe_attack == "Multi-Bite":
        enemy_attack_chance = Lernaean_Hydra["Attack Power"] + random.randint(1,20)
        print(f"The beast attacks with a {enemy_attack_chance}")
        if enemy_attack_chance >= Hercules["Armor Class"]:
            print("You have been struck!")
            Hercules["Health"] -= Multi_Bite(Lernaean_Hydra["Attack Power"])
        else:
            print("The lunging bite attack missed!")
    elif foe_attack == Tail_Whip:
        enemy_attack_chance = Lernaean_Hydra["Attack Power"] + random.randint(1,20)
        print(f"The beast attacks with a {enemy_attack_chance}")
        if enemy_attack_chance >= Hercules["Armor Class"]:
            print("You have been struck!")
            Hercules["Health"] -= Tail_Whip(Lernaean_Hydra["Attack Power"])
        else:
            print("The swinging tail attack missed!")

def Cerberus_attack(Hercules):                                              # Function for Cerberus' attacks against Herc
    print("Your enemy readies a vicious blow!")
    foe_attack = pick_random_attack(Cerberus["Attacks"])
    if foe_attack == "Multi-Bite":
        enemy_attack_chance = Cerberus["Attack Power"] + random.randint(1,20)
        print(f"The beast attacks with a {enemy_attack_chance}")
        if enemy_attack_chance >= Hercules["Armor Class"]:
            print("You have been struck!")
            Hercules["Health"] -= Multi_Bite(Cerberus["Attack Power"])
        else:
            print("The lunging bite missed!")
    elif foe_attack == "Pounce":
        enemy_attack_chance = Cerberus["Attack Power"] + random.randint(1,20)
        print(f"The beast attacks with a {enemy_attack_chance}")
        if enemy_attack_chance >= Hercules["Armor Class"]:
            print("You have been struck!")
            Hercules["Health"] -= Pounce(Cerberus["Attack Power"])
        else:
            print("With a great leap the beast pounces and misses you!")

def Attack(current_enemy):
    while Hercules["Health"] > 0 or current_enemy["Health"] > 0:
        Hercules_attack(current_enemy)
        if Hercules["Health"] < 0:
            print("You have died")
            break
        elif current_enemy["Health"] < 0:
            print(f"You have slain the {current_enemy['Name']}!")         
            break
        if current_enemy == Nemean_Lion:
            Nemean_Lion_attack(Hercules)
            if Hercules["Health"] < 0:
                print("You have died.")
                break
        elif current_enemy == Lernaean_Hydra:
            Lernaean_Hydra_attack(Hercules)
            if Hercules["Health"] < 0:
                print("You have died.")
                break
        elif current_enemy == Cerberus:
            Cerberus_attack(Hercules)
            if Hercules["Health"] < 0:
                print("You have died.")
                break   
        

Attack(Nemean_Lion)
