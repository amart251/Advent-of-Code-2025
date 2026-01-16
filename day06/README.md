# Day 6: Trash Compactor

## Part 1: Calculating the Grand Total

### Overview

Given a extra large grid containing numerical values and mathematical operations, the goal for today is to do some simple math. Each column of this grid represents a single calculation, where values are read **vertically** and combined using an operator from the bottom row, almost like a traditional math problem from grade school just without a line at the bottom separating the sum to calculation. The goal is to find the **grand total** of all column calculations. Sounds pretty simple enough. Just like in the previous day, we're going to implement recursion to both create the needed arrays and to make the calculations. 

### Input

- A grid with numerical values separated by varying amounts of whitespace
- Each row (except the last) contains operands
- The final row contains operators (`*` for multiplication or `+` for addition)
- Each column represents one complete calculation

**Example Grid:**
```
 123 328  51 64 
 45  64  387 23 
  6  98  215 314
 *   +   *   +  
```

### Logic

**Process**

1. **Parse the input** into separate rows using regex to remove the spacing between values
   - Create arrays for each row of numbers and the bottom operators

2. **Extract column data**
   - Select the corresponding vertical value from each number array to create a calculation
   - Place the operator between each of the numerical values

3. **Calculate each column** using recursion
   - Read numbers from bottom to top in each column
   - Solve for each calculation normally

4. **Grand total**
   - Sum the results from all columns to get the final result

### Parsing Example

**Original grid with varying spacing:**
```
 123 328  51 64 
 45  64  387 23 
  6  98  215 314
 *   +   *   +  
```

**After parsing using regex (removing the unneeded whitespaces):**
```
{123, 328,  51,  64}
{ 45,  64, 387,  23}
{  6,  98, 215, 314}
{  *,  +,   *,   +}
```

### Example

**Column 0:**
```
123
 45
  6
  *
```
Reading vertically: `123 * 45 * 6 = 33210`

**Column 1:**
```
328
 64
 98
  +
```
Reading vertically: `328 + 64 + 98 = 490`

**Column 2:**
```
 51
387
215
  *
```
Reading vertically: `51 * 387 * 215 = 4243455`

**Column 3:**
```
 64
 23
314
  +
```
Reading vertically: `64 + 23 + 314 = 401`

**Final Total**
As each column is calculated, the result is added to the **grand total**:

- Column 0: `123 * 45 * 6 = 33210` → Grand Total = `33210`
- Column 1: `328 + 64 + 98 = 490` → Grand Total = `66700`
- Column 2: `51 * 387 * 215 = 4243455` → Grand Total = `4,277,155`
- Column 3: `64 + 23 + 314 = 401` → Grand Total = `4,277,556`

**Result:** The grand total for all maths is `4,277,556` for this example

---

### Part 2: Cephalopod Math?

For this second part I was actually stumped for a bit on how to parse the input, since this time the whitespace between the numbers matters and so does the orientation of how each value is read. Normally the numerical values are read from top to bottom, but for part 2, each value is considered its own vertical column causing it to be built and read differently. To solve this, each integer of each number has to be placed into a a matrix to parse each character individually and calculate the new numbers differently.

### Parsing Approach

**Finding Column Boundaries**

Unlike Part 1 where we could strip whitespace, Part 2 requires preserving the exact spacing. The solution uses the operator positions as anchoring points:

1. **Locate operators** in the final line to determine column boundaries
2. **Extract columns as fixed-width sections** based on operator spacing
3. **Preserve all whitespace** within each column group—this spacing is crucial for Part 2

**Example Grid:**
```
 123 328  51 64 
 45  64  387 23 
  6  98  215 314
 *   +   *   +  
```

The operator positions determine exactly where each column begins and ends, acting as a sort of anchoring point for the matrix.

### Logic

**Matrix Construction and Transposition**

For each column:

1. **Extract the column content** as a series of string with the whitespace included
   - Each row contributes one string to this column
   - Whitespace within the string indicates digit positioning

2. **Create a character matrix** by converting each string to a list of characters and pad strings to equal length so the matrix is rectangular

3. **Transpose the matrix** using NumPy
   - Rows become columns and columns become rows allowing it to be read the proper way

4. **Read digits vertically** from the transposed matrix
   - Read down each transposed column
   - Remove spaces to form complete numbers
   - Only include non-empty results

5. **Calculate using recursion** 
   - Just like part 1, calculate the simple maths like usual to get the final result

### Example

**Original Grid:**
```
 123 328  51 64 
 45  64  387 23 
  6  98  215 314
 *   +   *   +  
```

**Column 0 (positions 0-2):**

Raw column content:
```
 123
 45
  6
```

Character matrix (before transpose):
```
Row 0: [ ,1,2,3]
Row 1: [ ,4,5, ]
Row 2: [ , ,6, ]
```

After transpose:
```
Col 0: [ ,  ,  ] → "" (empty)
Col 1: [1, 4,  ] → "14"
Col 2: [2,5, 6] → "256"
Col 3: [3, , ] → "3"
```

Reading vertically: `1 * 24 * 356 = 8544`

**Column 1 (positions 4-6):**

After constructing and transposing:
- Reading vertically: `369 + 248 + 8 = 625`

**Column 2 (positions 9-12):**

After constructing and transposing:
- Reading vertically: `32 * 581 * 175 = 3253600`

**Column 3 (positions 14-17):**

After constructing and transposing:
- Reading vertically: `623 + 432 + 4 = 1058`

**Final Total**

Using "Cephalopod Math" with the transposed matrix approach:

- Column 0: `1 * 24 * 356 = 8544` → Grand Total = `8544`
- Column 1: `369 + 248 + 8 = 625` → Grand Total = `9169`
- Column 2: `32 * 581 * 175 = 3253600` → Grand Total = `3262769`
- Column 3: `623 + 432 + 4 = 1058` → Grand Total = `3263827`

**Result:** The grand total using Cephalopod Math is `3263827` for this example
