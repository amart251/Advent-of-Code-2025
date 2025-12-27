# Day 1: Secret Entrance

# Python code to track position on a circular track from 0 to 99
# starting at position 50 and moving left or right based on input commands.
# Counts how many times the dial lands on and wraps around/passes by zero.


current_position = 50
is_zero = 0
times_zero_seen = 0

print("the dial's starting position is", current_position)

def process_command(command):
    global current_position, is_zero, times_zero_seen

    steps = int(command[1:])

    if 'L' in command:
        times_zero_seen += abs(steps) // 100
        remainder = -(steps % 100)
        new_position = current_position + remainder
        times_zero_seen +=1 if new_position <= 0 and new_position != remainder else 0
        
        current_position = (current_position - steps) % 100
        if current_position == 0:
            is_zero += 1

    elif 'R' in command:
        times_zero_seen += abs(steps) // 100
        remainder = steps % 100
        new_position = current_position + remainder
        times_zero_seen += 1 if new_position >= 100 else 0

        current_position = (current_position + steps) % 100
        if current_position == 0:
            is_zero += 1

with open("input.txt", "r") as file:
    for line in file:
        command = line.strip()
        process_command(command)



print("\nFinal Position:", current_position)
print("Times dial points at zero:", is_zero)
print("Number of times zero has been seen:", times_zero_seen)
