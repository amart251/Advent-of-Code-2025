# Day 3: The Lobby

## Part 1 Approach: Quick Stack Comparison

Similarly to the idea I initially had in the previous day, I thought it would be best to use the same idea with a different approach this time.

### Overview

Iterate through each digit in the string and compare it to values on a stack with a length of only two digits.

**Logic:**

- **Empty stack:** Push the first digit
- **One digit on stack:**
  - If next digit > current digit: Replace the current digit with the larger one
  - If next digit ≤ current digit: Push it onto the stack
  
- **Two digits on stack (full):**
  - If next digit > leading digit: Empty the stack and push the new leading digit
  - If next digit ≤ leading digit but > second digit: Replace the second digit
  - If next digit ≤ second digit: Ignore and continue

**Both conditions** check if the next digit is the final number in the string so that a comparison is made on the second digit rather than the leading one. This is to avoid only having one digit output in the final stack.

The final stack produces a two-digit number that is no larger than 99 since they are representing two batteries and their individual joltage levels.

### Example

**Input:**
```
12463483846441632 → 86
23423324572371345 → 77
89454582282344887 → 98
82384791873488291 → 99
```

**Result:** Sum total = 360 

This resulting sum (not this exact number) is what is needed to answer part 1