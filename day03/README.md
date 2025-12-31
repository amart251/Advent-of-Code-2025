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

---

## Part 2 Approach: Greedy Double Stack Comparison

Instead of looking for two digits, this time 12 are needed. Similarly to the previous logic with alterations, my approach would be to use greedy double stack comparisons.

### Overview

We build the result one digit at a time, always choosing the **largest digit available** within a range that guarantees enough remaining digits to complete 12 digits.

**Logic:**

1. Calculate how many more digits we need: `stack_limit = 12 - result_length`
2. Calculate how many digits are available: `have = string_length - current_position`
3. Search for the maximum digit in the range needed `[current_position, current_position + current - stack_limit]`
4. Select this maximum digit and shift forward in the main string
5. Repeat until there are 12 total digits

Since we need **12 digits for the answer**, it would be best to always have the stack at that length. If we need three more digits and have five available, we can search the first three positions (index 0-2), leaving positions 3-4 for the last two digits.

### Example

**Input:** `234234234234278` (15 digits)

**Process:**
- Position 0-3: [2,3,4,2] → max is 4 at index 2 → Select 4, continue from index 3
- Position 3-5: [2,3,4] → max is 4 at index 5 → Select 4, continue from index 6
- Continue greedily selecting the largest available digit...

**Output:** `434234234278` (12 digits)

### More Examples

| Input | Output |
|-------|--------|
| 987654321111111 | 987654321111 |
| 811111111111119 | 811111111119 |
| 234234234234278 | 434234234278 |
| 818181911112111 | 888911112111 |

**Result:** 3121910778619

This final sum (again, not this exact number) is the answer for part 2, thus completing all of day 3.