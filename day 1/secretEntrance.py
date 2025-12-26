# Part 1: Secret Entrance

# Python code to track position on a circular track from 0 to 99
# starting at position 50 and moving left or right based on input commands.
# Counts how many times the position wraps around zero.
# Example input: "L10", "R20"

current_position = 50
times_zero_seen = 0

print("the dial's starting position is", current_position)

def process_command(command):
    global current_position, times_zero_seen

    steps = int(command[1:])

    if 'L' in command:
        current_position = (current_position - steps) % 100
        if current_position == 0:
            times_zero_seen += 1
        # print("the dial is rotated", command, "to", current_position)

    elif 'R' in command:
        current_position = (current_position + steps) % 100
        if current_position == 0:
            times_zero_seen += 1
        # print("the dial is rotated", command, "to", current_position)

with open("input.txt", "r") as file:
    for line in file:
        command = line.strip()
        process_command(command)


print("\nFinal Position:", current_position)
print("Times dial points at zero:", times_zero_seen)

# Part 2: wip