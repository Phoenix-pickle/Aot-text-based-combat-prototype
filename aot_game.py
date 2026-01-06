import os      
import time      
import random      
      
      
def clear():      
    os.system('cls' if os.name == 'nt' else 'clear')      
      
characters = {      
    "levi": {      
        'name': 'Levi Ackerman',      
        'age': 30,      
        'city': 'Underground city',      
        'blood': 'Ackerman',      
        'power': 'Superhuman Strength',      
        'health': 100,      
        'stamina': 100,      
        'special_ability': 'Awakening',      
        'endurance': 100      
    },      
    "mikasa": {      
        'name': 'Mikasa Ackerman',      
        'age': 16,      
        'blood': 'Ackerman',      
        'power': 'Superhuman Strength',      
        'health': 100,      
        'stamina': 100,      
        'special_ability': 'Awakening',      
        'endurance': 100      
    },      
    "annie": {      
        'name': 'Annie Leonhart',      
        'age': 16,      
        'blood': 'A',      
        'power': 'Muay Thai',      
        'health': 100,      
        'special_ability': 'Titan shifter',      
        'stamina': 100,      
        'endurance': 100      
    },      
    "erwin": {      
        'name': 'Erwin Smith',      
        'age': 33,      
        'blood': 'A',      
        'power': 'Martial artist',      
        'health': 100,      
        'special_ability': 'Smart, decisive, manipulative',      
        'stamina': 100,      
        'endurance': 100      
      
    },      
    "hange": {      
        'name': 'Hange Zoe',      
        'age': 23,      
        'blood': 'B+',      
        'power': 'Exceptional intelligence, scientific knowledge, leadership skills',      
        'health': 100,      
        'special_ability': 'Good at using ODM',      
        'stamina': 100,      
        'endurance': 100      
    }      
}      
      
      
def display_bar(label, value, max_value, symbol="\u2588", length=20):      
    filled = int(value/max_value * length)       
    empty = length - filled       
    bar = symbol * filled + '-' * empty      
    return f"{label:<10} [{bar}] {value}/{max_value}"      
      
while True:      
    aot = input("Alright, maggot! Choose a character (Levi/Mikasa/Annie/Erwin/Hange):  And be quick about it Runt!:").lower()      
    player = characters.get(aot)      
      
    if player:      
        print("\n--- Your character's stats are ---")      
        for k, v in player.items():      
            print(f"{k.capitalize()}: {v}")      
              
        print("\n--- Status Bars ---")      
        print(display_bar("Health", player['health'], 100))      
        print(display_bar("Stamina", player['stamina'], 100))      
        print(display_bar("Endurance", player['endurance'], 100))      
    else:      
        print(f"HUH?!! WHAT CHARACTER IS '{aot.capitalize()}', IDIOT!")      
        continue  # Go back to the start of the loop if invalid choice      
      
    # Ask if player wants to change character      
    change = input("\nDo you wanna change your character, maggot? (yes/no): ").lower()      
      
    if change == "yes":      
        new_character = input(f"😤Ugh...fine. Which character do you want to replace {aot.capitalize()} with? (Levi/Mikasa/Annie/Erwin/Hange): ").lower()      
        playerr = characters.get(new_character)      
      
        if playerr:      
            print("\n--- Your new character's stats are ---")      
            for k, v in playerr.items():      
                print(f"{k.capitalize()}: {v}")      
                  
            print("\n--- Status Bars ---")      
            print(display_bar("Health:", playerr['health'], 100))      
            print(display_bar("Stamina:", playerr['stamina'], 100))      
            print(display_bar("Endurance:", playerr['endurance'], 100))      
                  
            player = playerr  # Update the player to the new character      
        else:      
            print("Oi! The character you chose doesn't exist. Titan ate 'em already!")      
    else:      
        print(f"You don't wanna replace {aot.capitalize()} with another character? Good. Or else you'd officially be on my sh*tlist!")      
          
    # Break loop after showing stats (either original or new character)      
    break      
      
weapons = {      
    "ODM Gear": {      
        'name': 'ODM Gear',      
        'weapon': 'Sword, Thunder Spear',      
        'durability': 100,       
    }      
}      
      
decision = input("\nAlright, cue ball. Do you wanna see the condition of your ODM Gear? (yes/no): ").lower()      
      
if decision == 'yes':      
    print("\n--- ⚙️ Your ODM Gears condition is  ---")      
    for k, v in weapons['ODM Gear'].items():      
        print(f"{k.capitalize()}: {v}")      
    time.sleep(2)      
      
print("\nRunt, get ready. Cause the Titans have Breached wall Rose!!")      
time.sleep(2)      
      
Wave = 1      
      
      
titan_stats = {      
    "HP": 100,      
    "HEIGHT": 20,      
    "Attack": 20      
}      
      
print(display_bar("\nTitan HP:", titan_stats['HP'], 100))      
print(display_bar("\nTitan Height:", titan_stats['HEIGHT'], 20))      
print(display_bar("\nTitan Attack:", titan_stats['Attack'], 20))      
      
while player['health'] > 0 and titan_stats['HP'] > 0:      
    clear()      
    print(f"\nWave {Wave}. {aot.capitalize()} is under attack! Don't you get eaten so easily, Runt!")      
      
    print(display_bar("Health", player['health'], 100))      
    print(display_bar("Stamina", player['stamina'], 100))      
    print(display_bar("Endurance", player['endurance'], 100))      
      
    print(display_bar("\nTitan HP", titan_stats['HP'], 100))      
      
    titan_damage = random.randint(10,titan_stats['Attack'])      
    player['health'] -= titan_damage      
    player['stamina'] -= 5      
    player['endurance'] -= 4      
      
    print(f"\nTitan hits {aot.capitalize()} for {titan_damage} damage!")      
      
    player_attack = random.randint(10,20)      
    titan_stats['HP'] -= player_attack      
    weapons['ODM Gear']['durability'] -= 1      
      
    print(f"\n{aot.capitalize()} strikes Titan for {player_attack} damage!")      
    print(display_bar("ODM Durability", weapons['ODM Gear']['durability'], 100))      
      
    time.sleep(2)      
    Wave += 1      
      
clear()      
if player['health'] <= 0:      
    print("Pathetic, you vermin! You got eaten by the Titan!")      
if titan_stats['HP'] <= 0:      
    print("Oh, you actually won? You're not as bad as i thought you'd be, shrimp! Well done!")
