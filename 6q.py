import time
import os
import math

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_track(achilles_position, tortoise_position, track_length):
    # Create the track as a list of '-'
    achilles_track = ['-' for _ in range(track_length)]
    tortoise_track = ['-' for _ in range(track_length)]

    # Set the start and end positions
    achilles_track[0] = '<'
    achilles_track[-1] = '>'
    tortoise_track[0] = '<'
    tortoise_track[-1] = '>'

    # Set the positions of Achilles and the tortoise
    achilles_track[math.floor(achilles_position)] = 'A'
    tortoise_track[math.floor(tortoise_position)] = 'T'

    # Print the track
    print('Achilles: ' + ''.join(achilles_track))
    print('Tortoise: ' + ''.join(tortoise_track))

def move_achilles(achilles_position, tortoise_position):
    # Move Achilles half the remaining distance
    return achilles_position + (tortoise_position - achilles_position) / 2

def move_tortoise(tortoise_position):
    # Move the tortoise at a constant speed
    return tortoise_position + 1

# Creation of a starting message with some transition animation
def starting_message():
    # Clear the terminal and show the initial message
    clear_terminal()
    print("Zeno's Paradox of Achilles and the Tortoise")
    time.sleep(1)
    clear_terminal()
    time.sleep(0.5)
    print("Starting Race!")
    time.sleep(1)
    clear_terminal()
    time.sleep(0.5)
    print("Ready...")
    time.sleep(1)
    clear_terminal()
    time.sleep(0.5)
    print("Set...")
    time.sleep(1)
    clear_terminal()
    time.sleep(0.5)
    print("Go!!!")
    time.sleep(1)
    clear_terminal()
    time.sleep(0.5)

# Creation of a ending message with some transition animation
def ending_message():
    time.sleep(0.5)
    clear_terminal()
    print("Unfortunatly Achilles will never pass Tortoise at this experiment... =(")
    time.sleep(1)
    clear_terminal()
    print("Demonstration terminated, thank you for your attention!")
    time.sleep(1)
    clear_terminal()

def run_race():
    # Length of the track
    track_length = 50

    # Head start of the tortoise
    head_start = 10

    # Create the initial positions of Achilles and the tortoise
    achilles_position = 0
    tortoise_position = head_start

    starting_message()

    # While Achilles has not caught up with the tortoise
    while achilles_position < track_length and tortoise_position < track_length:
        clear_terminal()

        print_track(achilles_position, tortoise_position, track_length)

        # Wait for a bit
        time.sleep(0.2)

        tortoise_position = move_tortoise(tortoise_position)
        achilles_position = move_achilles(achilles_position, tortoise_position)

    ending_message()

# Call the function to start the race
run_race()
