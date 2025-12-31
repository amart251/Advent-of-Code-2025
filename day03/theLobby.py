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

def find_more_batteries(digits_str):
    i = 0
    joltage_stack = []
    if len(digits_str) < 13:
        return 0
    
    while len(joltage_stack) < 12:

        stack_limit = 12 - len(joltage_stack)
        have = len(digits_str) - i
        
        if have < stack_limit:
            joltage_stack.extend([int(d) for d in digits_str[i:]])
            break

        max_digit = -1
        max_index = -1
        for j in range(i, i + have - stack_limit + 1):
            if int(digits_str[j]) > max_digit:
                max_digit = int(digits_str[j])
                max_index = j
        
        joltage_stack.append(max_digit)
        i = max_index + 1
    
    if len(joltage_stack) == 12:
        return int(''.join(str(d) for d in joltage_stack))
    
    return 0


with open("input.txt", "r") as f:
    battery_bank = f.read().strip()
lines = battery_bank.split()


total_joltage = 0
final_large_joltage = 0

for line in lines:
    if line:
        largest_two_batteries = find_largest_two_digit(line.strip())
        largest_battery_set = find_more_batteries(line.strip())
        total_joltage += largest_two_batteries
        final_large_joltage += largest_battery_set

print(f"Total output joltage from two batteries is: {total_joltage}")
print(f"Total output joltage from 12 batteries is: {final_large_joltage}")