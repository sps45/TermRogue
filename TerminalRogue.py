from art import *
from random import randrange
import time
import numpy as np

def spacer(count):
    for x in range(count):
        print()


tprint("Term Rogue")
spacer(2)
print("You woke to the suffocating scent of wet earth and rot, bruises")
print("throbbing beneath layers of grime. The trees huddle close around,")
print("their gnarled branches twisting like skeletal fingers, blocking")
print(" out the daylight in a sinister embrace")
print()
print("                              ...                                ")
print()

print()
#time.sleep(7)


print("You had no memory of how you got there, only chilling certainty")
print("that something was watching you from the shadows just beyond the")
print("clearing.")
print("                              ...                                ")
spacer(3)
#time.sleep(4)


print("From the shadows, a figure emerged - an old man with wild silver")
print("hair, and eyes that seemed to hold the secrets of the forest. He")
print("stepped closer, his voice a low, gravelly whisper.")
spacer(2)
print("MYSTERIOUS OLD MAN: \"Do you remember your name?\"")
spacer(2)

player_name = input("> Enter your name: ")


print("                              ...                                ")

print()

print("MYSTERIOUS OLD MAN: Well " + player_name + ", I know you're probably")
print("wondering how you got here, but the details of your arrival matter not;")
print("what lies ahead is a battle unlike any you've known...")

print()
print("                              ...                                ")
spacer(2)
#time.sleep(5)


print("The old man raises his hand, and the forest erupts with a sudden")
print("blaze of light, revealing three weapon chests nestled among the")
print("ancient trees")

spacer(2)

print("[1] Red chest")
print("[2] Blue chest")
print("[3] Green chest")

print()


while True:
    try:
        chest_choice = int(input("> Select a chest: "))
        if 1 <= chest_choice <= 3:
            break
        raise Exception()
    except:
        print("Invalid option")
print()
print()
print("You open the chest and strap on the weathered defense, its leather straps")
print("creaking with age, the metal plates cool and heavy against your bruised")
print("skin.") 
print()
print("As you adjusted the final piece, your gaze caught a faint glimmer")
print("in the shadows—a small tunnel near the chests, half-hidden by the tangled")
print("roots, its entrance dark and foreboding")

print()
print("                              ...                                ")
spacer(2)
#time.sleep(8)

print()


print("As you took your first step into the tunnel, the old man's laughter echoed")
print("through the clearing - a low, sinister sound that sent a shiver down your")
print("spine.")
print()
print("The moment you crossed the threshold, the tree vines slithered to life,")
print("twisting and writhing untl they sealed the entrance behind you, plunging the")
print("tunnel into darkness")
print()

#time.sleep(5)

print()
print("                              ...                                ")

spacer(2)
print("As you attempt to get a grasp on your surroundings, a 2-headed Goblin")
print("confronts you with its weapon drawn!")
print()

class Character:
    def __init__(self, name, health, attack_power, defense, base_defense, healthpots):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.base_defense = base_defense # Defense level before any buffs of debuffs
        self.healthpots = healthpots

    def take_damage(self, damage):
        # Defense reduces damage
        reduced_damage = max(0, damage - self.defense)
        self.health -= reduced_damage
        print(f"{self.name} takes {reduced_damage} damage! HP remaining:", max(0,self.health))

    def defend(self, target):
        # Boosts the defense value of target. 
        def_boost = 5
        if self.defense <= self.base_defense:
            self.defense += def_boost
            print(f"{self.name} feels their armor thicken. Their defense is" \
                  " raised by", def_boost)

    def heal(self, target):
        heal_amount = randrange(25, 35)
        self.health = min(100, self.health + heal_amount)
        self.healthpots -= 1 
        print(f"{self.name} heals for {heal_amount}. Their HP is now {self.health}")
        print()

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")

        target.take_damage(self.attack_power)



player = Character(name =player_name, health=100, attack_power=np.random.choice([25, 20, 0], p=[0.1, 0.8, 0.1]), defense=5, base_defense=5, healthpots=2)
enemy = Character(name="Goblin", health=100, attack_power=np.random.choice([25, 20, 0], p=[0.1, 0.7, 0.2]), defense=5, base_defense=5, healthpots=2)


turn = 0

 
def player_turn():
    print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +")
    print()
    print("-->", player.name + ":", player.health, "HP,", player.defense, "DEF")
    print()
    print("-->", enemy.name + ":", enemy.health, "HP,", enemy.defense, "DEF")
    print()
    print("[1] Attack")
    print("[2] Defend")
    print(f"[3] Healing Potion ({player.healthpots} remaining)")
    print()

    turn_choice = input("> ")

    print()

    if turn_choice.isdigit() and 0 < int(turn_choice) < 4:
    # Check if turn_choice is a digit before converting it to integer
        turn_choice = int(turn_choice)
        if turn_choice == 1:
            player.attack(enemy)
            print()
            #time.sleep(1)
        elif turn_choice == 2:
            player.defend(player)
            print()
            #time.sleep(1)
        elif turn_choice == 3:
            if player.healthpots != 0:
                player.heal(player)
                print(f"{player.name} has {player.healthpots} potions remaining")
                #time.sleep(1)
            else:
                print(f"{player.name} reaches for a healing potion, but none remain!")
                print()
                    

    if (enemy.defense > enemy.base_defense):
                enemy.defense = enemy.base_defense
                print(f"{enemy.name}'s defense has returned to normal")
                print()

def enemy_turn():
    print("+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +")
    print()
    print(f"{enemy.name} readies their weapon...")
    print()
    print()
    print("-->", player.name + ":", player.health, "HP,", player.defense, "DEF")
    print()
    print("-->", enemy.name + ":", enemy.health, "HP,", enemy.defense, "DEF")
    print()
    print()
    #time.sleep(1)

    enemy_turn_choice = np.random.choice([1, 2, 3], p=[0.6, 0.2, 0.2])
    # Enemy will make their choice based on a percentage chance

    if enemy_turn_choice == 1:
        enemy.attack(player)
        print()
        #time.sleep(1)
    elif enemy_turn_choice == 2:
        enemy.defend(enemy)
        print()
        #time.sleep(1)
    elif enemy_turn_choice == 3:
        enemy.heal(enemy)
        print()
        #time.sleep(1)
    
    if (player.defense > player.base_defense):
            player.defense = player.base_defense
            print(f"{player.name}'s defense has returned to normal")
            print()

turn = 0
# Turn 0 is the player's turn. Turn 1 is the AI's turn. The loop below will iterate between 0 and 1

while True:
    if player.health > 0 and enemy.health > 0:
        if turn == 0:
            player_turn()
            turn += 1
        elif turn == 1:
            enemy_turn()
            turn -= 1
    else:
        if player.health > enemy.health:
            print(player.name, "has won the battle")
            break
        else:
            print(enemy.name, "has won the battle")
            break

print("Press the Enter key to exit")       
input()