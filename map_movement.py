import numpy as np
from pynput import keyboard
import random
import sys
import os

past_cords = [(12,50)]

def print_map():
    for line in map_array:
        for value in line:
            if value == 1:
                print("#", end="")
            elif value == 0:
                print(" ", end="")
            elif value == 2:
                print("o", end="")
            elif value == 3:
                print("#", end="")
            elif value == 4:
                print(" ", end="")
        print("")

def gen_random(chance):
    wall_chance = chance
    random_num = random.random()
    if random_num < wall_chance:
        return True
    else:
        return False

def check_zero(array, num):
    if array == 0:
        return num
    else:
        return array

def move_up(player_y, player_x,top_percent,left_percent,right_percent):
    if map_array[player_y-1][player_x] == 0 or map_array[player_y-1][player_x] == 4:
        map_array[player_y][player_x] = 0
        player_y -= 2
        if (player_y, player_x) not in past_cords:
            past_cords.append((player_y, player_x))
            #top
            if not gen_random(top_percent):
                map_array[player_y - 1][player_x] = check_zero(map_array[player_y - 1][player_x],1)
                map_array[player_y - 1][player_x - 1] = check_zero(map_array[player_y - 1][player_x - 1],1)
                map_array[player_y - 1][player_x + 1] = check_zero(map_array[player_y - 1][player_x + 1],1)
            else:
                map_array[player_y - 1][player_x] = check_zero(map_array[player_y - 1][player_x],4)
                map_array[player_y - 1][player_x - 1] = check_zero(map_array[player_y - 1][player_x - 1],3)
                map_array[player_y - 1][player_x + 1] = check_zero(map_array[player_y - 1][player_x + 1],3)
            #left
            if not gen_random(left_percent):
                map_array[player_y][player_x - 1] = check_zero(map_array[player_y][player_x - 1],3)
            else:
                map_array[player_y][player_x - 1] = check_zero(map_array[player_y][player_x - 1],4)
            #right
            if not gen_random(right_percent):
                map_array[player_y][player_x + 1] = check_zero(map_array[player_y][player_x + 1],3)
            else:
                map_array[player_y][player_x + 1] = check_zero(map_array[player_y][player_x + 1],4)

        map_array[player_y][player_x] = 2
    return player_y


def move_down(player_y, player_x,down_percent,left_percent,right_percent):
    if map_array[player_y + 1][player_x] == 0 or map_array[player_y + 1][player_x] == 4:
        map_array[player_y][player_x] = 0
        player_y += 2
        if (player_y, player_x) not in past_cords:
            past_cords.append((player_y, player_x))
            #top
            if not gen_random(down_percent):
                map_array[player_y + 1][player_x] = check_zero(map_array[player_y + 1][player_x],1)
                map_array[player_y + 1][player_x - 1] = check_zero(map_array[player_y + 1][player_x - 1],1)
                map_array[player_y + 1][player_x + 1] = check_zero(map_array[player_y + 1][player_x + 1],1)
            else:
                map_array[player_y + 1][player_x] = check_zero(map_array[player_y + 1][player_x],4)
                map_array[player_y + 1][player_x - 1] = check_zero(map_array[player_y + 1][player_x - 1],3)
                map_array[player_y + 1][player_x + 1] = check_zero(map_array[player_y + 1][player_x + 1],3)
            #left
            if not gen_random(left_percent):
                map_array[player_y][player_x - 1] = check_zero(map_array[player_y][player_x - 1],3)
            else:
                map_array[player_y][player_x - 1] = check_zero(map_array[player_y][player_x - 1],4)
            #right
            if not gen_random(right_percent):
                map_array[player_y][player_x + 1] = check_zero(map_array[player_y][player_x + 1],3)
            else:
                map_array[player_y][player_x + 1] = check_zero(map_array[player_y][player_x + 1],4)

        map_array[player_y][player_x] = 2
    return player_y


def move_left(player_y, player_x,top_percent,down_percent,left_percent):
    if map_array[player_y][player_x - 1] == 0 or map_array[player_y][player_x - 1] == 4:
        map_array[player_y][player_x] = 0
        player_x -= 2
        if (player_y, player_x) not in past_cords:
            past_cords.append((player_y, player_x))

            # bottom
            if not gen_random(down_percent):
                map_array[player_y + 1][player_x] = check_zero(map_array[player_y + 1][player_x],1)
                map_array[player_y + 1][player_x - 1] = check_zero(map_array[player_y + 1][player_x + 1],1)
            else:
                map_array[player_y + 1][player_x] = check_zero(map_array[player_y + 1][player_x],4)
                map_array[player_y + 1][player_x - 1] = check_zero(map_array[player_y + 1][player_x - 1],3)
            # top
            if not gen_random(top_percent):
                map_array[player_y - 1][player_x] = check_zero(map_array[player_y - 1][player_x],1)
                map_array[player_y - 1][player_x - 1] = check_zero(map_array[player_y - 1][player_x - 1],1)
            else:
                map_array[player_y - 1][player_x] = check_zero(map_array[player_y - 1][player_x],4)
                map_array[player_y - 1][player_x - 1] = check_zero(map_array[player_y + 1][player_x - 1],1)
            # left
            if not gen_random(left_percent):
                map_array[player_y][player_x - 1] = check_zero(map_array[player_y][player_x - 1], 3)
            else:
                map_array[player_y][player_x - 1] = check_zero(map_array[player_y][player_x - 1], 4)

        map_array[player_y][player_x] = 2
    return player_x


def move_right(player_y, player_x,top_percent, down_percent, right_percent):
    if map_array[player_y][player_x + 1] == 0 or map_array[player_y][player_x + 1] == 4:
        map_array[player_y][player_x] = 0
        player_x += 2
        if (player_y, player_x) not in past_cords:
            past_cords.append((player_y, player_x))
            # bottom
            if not gen_random(down_percent):
                map_array[player_y + 1][player_x] = check_zero(map_array[player_y + 1][player_x],1)
                map_array[player_y + 1][player_x + 1] = check_zero(map_array[player_y + 1][player_x + 1],1)
            else:
                map_array[player_y + 1][player_x] = check_zero(map_array[player_y + 1][player_x],4)
                map_array[player_y + 1][player_x + 1] = check_zero(map_array[player_y + 1][player_x + 1],3)
            # top
            if not gen_random(top_percent):
                map_array[player_y - 1][player_x] = check_zero(map_array[player_y - 1][player_x],1)
                map_array[player_y - 1][player_x + 1] = check_zero(map_array[player_y - 1][player_x + 1],1)
            else:
                map_array[player_y - 1][player_x] = check_zero(map_array[player_y - 1][player_x],4)
                map_array[player_y - 1][player_x + 1] = check_zero(map_array[player_y - 1][player_x + 1],3)
            # right
            if not gen_random(right_percent):
                map_array[player_y][player_x + 1] = check_zero(map_array[player_y][player_x + 1], 3)
            else:
                map_array[player_y][player_x + 1] = check_zero(map_array[player_y][player_x + 1], 4)

        map_array[player_y][player_x] = 2
    return player_x


player_x = 50
player_y = 12


def on_key_press(key):
    global player_x
    global player_y
    top_percent = 0.4
    left_percent = 0.75
    right_percent = 0.75
    down_percent = 0.4
    # need to make a clause to check for 1s making a border
    try:
        if key.char == "w":
            player_y = move_up(player_y, player_x,top_percent,left_percent,right_percent)
            if player_y > 0:
                print_map()
            elif player_y == 0:
                map_array[0][player_x] = 1
                player_y = 2

        if key.char == "s":
            player_y = move_down(player_y, player_x,down_percent,left_percent,right_percent)
            print_map()

        if key.char == "a":
            player_x = move_left(player_y, player_x,top_percent,down_percent,right_percent)
            if player_x > 0:
                print_map()
            elif player_x == 0:
                map_array[player_y][0] = 1
                player_x = 2

        if key.char == "d":
            player_x = move_right(player_y, player_x,top_percent,down_percent,left_percent)
            print_map()

    except AttributeError:
        return False
    except IndexError:
        if player_x < 0:
            player_x += 2
            print_map()
        elif player_x > 50:
            player_x -= 2
            print_map()
        elif player_y < 0:
            player_y += 2
            print_map()
        elif player_y > 100:
            player_y -= 2
            print_map()



# Set up listeners
def map_movement():
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

    # Suppress console output
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')

    # Keep the program running
    listener.join()

    # Restore console output
    sys.stdout.close()
    sys.stdout = original_stdout


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

    new_arr[11][49] = 3
    new_arr[11][51] = 3
    new_arr[13][49] = 3
    new_arr[13][51] = 3
    new_arr[12][50] = 2

    return new_arr




array_size = (25, 100)
map_array = np.zeros(array_size)
map_array = surround_with_ring(map_array)
print_map()
map_movement()

