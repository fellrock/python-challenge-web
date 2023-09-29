import random

def drop_egg(floor, breaking_floor):
    """Simulates dropping an egg from a certain floor."""
    return floor >= breaking_floor

def find_breaking_floor(max_floor, num_eggs):
    """Finds the breaking floor using the strategy described above."""
    step = 14
    current_floor = 0
    while current_floor <= max_floor and num_eggs > 1:
        current_floor += step
        step -= 1
        if drop_egg(current_floor, breaking_floor):
            num_eggs -= 1
            current_floor -= step
            break
    if num_eggs == 1:
        for floor in range(current_floor + 1, min(current_floor + step + 2, max_floor + 1)):
            if drop_egg(floor, breaking_floor):
                return floor
    return current_floor

# Define the total number of floors and eggs
total_floors = 100
total_eggs = 2

# Choose a random floor as the breaking floor
breaking_floor = random.randint(1, total_floors + 1)

# Find the breaking floor using the strategy described above
found_floor = find_breaking_floor(total_floors, total_eggs)

print(f"Randomly chosen breaking floor: {breaking_floor}")
print(f"Breaking floor found by the algorithm: {found_floor}")
