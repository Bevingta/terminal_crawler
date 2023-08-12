def print_banner():
    with open('banner.txt') as banner:
        for line in banner:
            print(line, end='')


print_banner()

import random
import numpy as np
from walking_description import walking_descriptions


# gets the stats of the generated character
class Character:
    def __init__(self, name):
        self.name = name
        self.current_health = 100
        self.max_health = 100
        self.dfence = 0
        self.shield = 10
        self.attack = 50
        self.crit = 50
        self.dodge = 0
        self.freeze = 0
        self.burn = 0
        alive = True


# prints the current stats of the called character
def print_stats(character):
    print(f"Max Health: {character.max_health}")
    print(f"Current Health: {character.current_health}")
    print(f"Defense: {character.dfence}")
    print(f"Attack: {character.attack}")
    print(f"Crit Chance: {character.crit}%")
    print(f"Dodge Chance: {character.dodge}%")
    print(f"Freeze Chance: {character.freeze}%")
    print(f"Burn Chance: {character.burn}%")


def update_health(reciever, damage):
    reciever.current_health -= damage
    print(f"{reciever.name} was hit for {damage} points of damage.")
    if reciever.current_health <= 0:
        print(f"{reciever.name} is dead.")
        in_combat = False
        return in_combat
    else:
        print(f"{reciever.name}'s current health: {reciever.current_health}")


def display_health():
    player_tick_value = player.max_health // 10
    enemy_tick_value = enemy.max_health // 10
    player_ticks = ['[', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ']']
    enemy_ticks = ['[', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ']']

    # calculates the health loss against the value of each tick and removes one tick for each step
    player_health_loss = (player.max_health - player.current_health) // player_tick_value
    i = -2
    r = 0
    while r < (player_health_loss) and i > -12:
        player_ticks[i] = ' '
        i -= 1
        r += 1
    r = 0
    enemy_health_loss = (enemy.max_health - enemy.current_health) // enemy_tick_value
    i = -2
    r = 0
    while r < (enemy_health_loss) and i > -12:
        enemy_ticks[i] = ' '
        i -= 1
        r += 1
    print(f"{player.name}:", end="")
    for char in player_ticks:
        print(char, end="")
    if player.current_health > 0:
        print(f"({player.current_health}/{player.max_health})", end="")
    if player.current_health <= 0:
        print(f":0/{player.max_health})", end="")

    print("                ", end="")
    print(f"{enemy.name}:", end="")
    for char in enemy_ticks:
        print(char, end="")
    if enemy.current_health > 0:
        print(f"({enemy.current_health}/{enemy.max_health})")
    else:
        print(f"(0/{enemy.max_health})")
    print('')


# need to add in crit and burn and all that
def calculate_damage(attacker, reciever):
    damage = attacker.attack
    damage = calculate_crit(attacker, damage)
    return (damage)


def calculate_crit(attacker, damage):
    crit_chance = attacker.crit * .01
    random_int = random.random()
    if random_int < crit_chance:
        damage = damage * 1.5
        return damage
    else:
        return damage


def block(blocker, attacker):
    damage = calculate_damage(attacker, blocker)
    damage = attacker.attack - damage
    if damage > 0:
        update_health(blocker, damage)
    else:
        print("Attack was fully blocked")


def attack(attacker, reciever):
    damage = calculate_damage(attacker, reciever)
    status = update_health(reciever, damage)
    return status


def calc_in_combat():
    if player.current_health <= 0:
        return False
    elif enemy.current_health <= 0:
        return False
    else:
        return True


def combat():
    turn = 'player'
    display_health()
    in_combat = True
    while in_combat == True:
        if turn == 'player':
            user_choice = input("[a] Attack            [b] Block           [f] Flee\nAction: ").lower()
            if user_choice == 'a':
                # make a delay inbetween prints
                # make an animation?
                attack(player, enemy)
                display_health()
                in_combat = calc_in_combat()  # could make this a function
                turn = 'enemy'

            elif user_choice == 'b':
                block(player, enemy)  # have to fix the block bc it could not attack sometimes
                display_health()
                in_combat = calc_in_combat()
                turn = 'enemy'

            elif user_choice == 'f':
                print("Fleeing")
                in_combat = False
        elif turn == 'enemy':
            print("Enemy attacks:")
            attack(enemy, player)
            display_health()
            in_combat = calc_in_combat()
            turn = 'player'


def exploration():
    while in_combat == False:
        None


enemy_name_list = ["Skeleton"]
enemy_file_list = ["skeleton_with_sword.txt"]


def generate_enemy():
    enemy_num = random.randint(0, 1 - len(enemy_file_list))
    with open(enemy_file_list[enemy_num]) as enemy_icon:
        for line in enemy_icon:
            print(line, end="")
    enemy = Character(enemy_name_list[enemy_num])


def print_banner():
    with open('banner.txt') as banner:
        for line in banner:
            print(line, end='')


def surround_with_ring(arr):
    m, n = arr.shape
    new_arr = np.copy(arr)

    # Top row
    new_arr[0, :] = 1

    # Bottom row
    new_arr[m - 1, :] = 1

    # Left column
    new_arr[:, 0] = 1

    # Right column
    new_arr[:, n - 1] = 1

    return new_arr


array_size = (50, 100)
map_array = np.zeros(array_size)
map_array = surround_with_ring(map_array)
print(map_array)

print_banner()

player_name = print(input("Enter your name: "))
player = Character(player_name)
player.current_health = 100
player.max_health = 100
player.dfence = 10
print_stats(player)

enemy = Character("Orc")
# need to make in_combat a global term which can be triggered if __combat__ == True (don't know how to initialize it)


generate_enemy()
# combat()
