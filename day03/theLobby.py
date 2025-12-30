# Day 3: The Lobby

def find_largest_two_digit(digits_str):
    joltage_stack = []
    
    for digit_index, digit_char in enumerate(digits_str):
        digit = int(digit_char)
        is_last_digit = (digit_index == len(digits_str) - 1)
        
        if len(joltage_stack) == 0:
            joltage_stack.append(digit)
        
        elif len(joltage_stack) == 1:
            if is_last_digit:
                joltage_stack.append(digit)
            elif digit > joltage_stack[0]:
                joltage_stack[0] = digit
            else:
                joltage_stack.append(digit)
        
        else:
            if is_last_digit:
                if digit > joltage_stack[1]:
                    joltage_stack[1] = digit
            elif digit > joltage_stack[0]:
                joltage_stack = [digit]
            elif digit > joltage_stack[1]:
                joltage_stack[1] = digit
    
    if len(joltage_stack) == 2:
        return int(str(joltage_stack[0]) + str(joltage_stack[1]))
    elif len(joltage_stack) == 1:
        return joltage_stack[0]
    return 0


with open("input.txt", "r") as f:
    battery_bank = f.read().strip()
lines = battery_bank.split()

total_joltage = 0

for line in lines:
    if line:
        largest_two_batteries = find_largest_two_digit(line.strip())
        # print(f"{line} → {largest_two_batteries}")
        total_joltage += largest_two_batteries

print(f"\nTotal output joltage is: {total_joltage}")
