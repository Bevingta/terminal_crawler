from map_movement import generate_map, print_map, map_movement


def print_banner():
    with open('graphics/banner.txt') as banner:
        for line in banner:
            print(line, end='')

print_banner()

#create character in here

map_array = generate_map()

print_map()

map_movement()