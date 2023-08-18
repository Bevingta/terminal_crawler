import sys
import random
import time
from starting_quest import starting_descriptions
from enemy_lists import enemy_name_list,enemy_file_list

enemies_killed = [0]
xp_gained = [0]
next_level_xp = [10]
final_score = [0]



def print_game_over():
    with open('graphics/game_over.txt') as banner:
        print("")
        print("")
        for line in banner:
            print(line, end='')
            time.sleep(0.1)
        print("")
        print("")
        print("")

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
        self.xp_drop = 0
        self.stamina = 5
        alive = True

# prints the current stats of the called character
def print_stats(character):
    print(f"Max Health: {character.max_health}")
    time.sleep(0.3)
    print(f"Current Health: {character.current_health}")
    time.sleep(0.3)
    print(f"Defense: {character.dfence}")
    time.sleep(0.3)
    print(f"Attack: {character.attack}")
    time.sleep(0.3)
    print(f"Crit Chance: {character.crit}%")
    time.sleep(0.3)
    print(f"Dodge Chance: {character.dodge}%")
    time.sleep(0.3)
    print(f"Freeze Chance: {character.freeze}%")
    time.sleep(0.3)
    print(f"Burn Chance: {character.burn}%")
    time.sleep(0.3)
    print("")
    print("")

def update_health(receiver, damage):
    receiver.current_health -= damage
    print(f"{receiver.name} was hit for {damage} points of damage.")
    if receiver.current_health <= 0:
        print(f"{receiver.name} is dead.")
        in_combat = False
        return in_combat
    else:
        print(f"{receiver.name}'s current health: {receiver.current_health}")


def display_health(player, enemy):
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
def calculate_damage(attacker, receiver):
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


def attack(attacker, receiver):
    damage = calculate_damage(attacker, receiver)
    status = update_health(receiver, damage)
    return status


def end_game():
    print_game_over()
    print(f"Enemies Killed: {enemies_killed[0]}")
    print(f"XP Gained: {xp_gained[0]}")
    print(f"Final Score: {final_score[0]}")
    sys.exit()

def level_up(player):
    with open("graphics/level_up.txt") as level_up:
        for line in level_up:
            print(line,end="")
            time.sleep(0.05)
    player.attack += 5
    player.max_health += 20
    player.stamina += 2
    print("New Stats: ")
    print_stats(player)

def calc_in_combat(player, enemy):
    if player.current_health <= 0:
        end_game()
    elif enemy.current_health <= 0:
        enemies_killed[0] = enemies_killed[0] + 1
        xp_gained[0] = xp_gained[0] + enemy.xp_drop
        if xp_gained[0] > next_level_xp[0]:
            level_up(player)
        return False
    else:
        return True


def combat(player, enemy):
    turn = 'player'
    display_health(player,enemy)
    in_combat = True
    while in_combat:
        if turn == 'player':
            user_choice = input("[a] Attack            [b] Block           [f] Flee\nAction: ").lower()
            if user_choice == 'a':
                # make a delay inbetween prints
                # make an animation?
                attack(player, enemy)
                display_health(player,enemy)
                in_combat = calc_in_combat(player,enemy)  # could make this a function
                turn = 'enemy'

            elif user_choice == 'b':
                block(player, enemy)  # have to fix the block bc it could not attack sometimes
                display_health(player, enemy)
                in_combat = calc_in_combat(player, enemy)
                turn = 'enemy'

            elif user_choice == 'f':
                print("Fleeing")
                in_combat = False
        elif turn == 'enemy':
            print("Enemy attacks:")
            attack(enemy, player)
            display_health(player, enemy)
            in_combat = calc_in_combat(player, enemy)
            turn = 'player'

def generate_player():
    rand = random.randint(0, len(starting_descriptions)-1)
    print(starting_descriptions[rand])
    print("")
    player_name = input("Enter your name: ")
    player = Character(player_name)
    player.current_health = 100
    player.max_health = 100
    player.dfence = 10
    print_stats(player)
    return player

def generate_stats(enemy, player, xp):
    enemy.attack = random.randint(int((0.75*player.attack)), int((1.25*player.attack)))
    enemy.xp_drop = xp
    enemy.max_health = random.randint(int(0.5*player.max_health),int(0.75*player.max_health))
    enemy.current_health = enemy.max_health

def generate_enemy(player, num):
    if num == 5:
        rand_index = random.randint(0, len(enemy_name_list))
        enemy = enemy_name_list[rand_index]
        enemy_file = enemy_file_list[rand_index]
        print("")
        print("")
        with open(enemy_file) as enemy_drawing:
            for line in enemy_drawing:
                print(line, end="")
                time.sleep(0.1)
        enemy = Character(enemy)
        generate_stats(enemy, player, 10)
        print(enemy.name)
        print_stats(enemy)
        combat(player, enemy)
        return enemy

