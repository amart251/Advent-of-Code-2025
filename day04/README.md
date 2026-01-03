# Day 4: Printing Department

First off, **Happy New Year!**
2025 has been a crazy experience post-graduation that I couldn't have otherwise found myself thinking of doing. Traveled and experienced new places and met new faces that I wouldn't have thought about ten years ago.
If last year is any indication of how things are going to fly, then I'm on board for what's next this 2026, through the highs and the lows.

## Part 1: Finding Accessible Paper Rolls

### Overview

Find out if certain characters, are valid for removal based on it's eight surrounding adjacent value. In the context of the story, find out if the forklifts can easily access the rolls of paper on the shelves.

**Processing**
- Read the text file and convert it into a 2D array called `paper_map`
- Each sub-array represents a row from the input
- Each character in the row represents a position

**Logic:**
1. For each position with a `@` (roll of paper):
   - Count how many `@` symbols are in the 8 adjacent positions
   - If there are **fewer than 4** adjacent rolls, increment `roll_counter` by 1
   - If there are **4 or more** adjacent rolls, the roll is not counted

2. **Boundary handling**: 
   - Out-of-bounds positions are treated as `.` (empty spaces)
   - They do NOT count toward the 4 adjacent rolls requirement

### Symbols
- `@` = A roll of paper
- `.` = An empty location

### Grid Positioning

For any given position `(x, y)`, we check 8 adjacent positions:

| Position   | Coordinates |
|------------|-------------|
| Top Left   | (x-1, y-1)  |
| Up         | (x, y-1)    |
| Top Right  | (x+1, y-1)  |
| Left       | (x-1, y)    |
| **Center** | **(x, y)**  |
| Right      | (x+1, y)    |
| Bottom Left| (x-1, y+1)  |
| Down       | (x, y+1)    |
| Bottom Right| (x+1, y+1) |

**Visual representation:**
```
(x-1,y-1) | (x, y-1) | (x+1,y-1)
----------|----------|----------
(x-1, y)  | (x, y)   | (x+1, y)
----------|----------|----------
(x-1,y+1) | (x,y+1)  | (x+1,y+1)
```

3. **Output**: Print the total number of accessible rolls of paper

### Example

**Initial Grid:**

```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
```

**Validated Grid (x marks valid positions):**

```
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
```

---

## Part 2: Removing Even More Paper Rolls

### Process

This second part is essentially the same as the first, however with one adjustment.

1. When a roll of paper is found (fewer than 4 adjacent rolls):
   - **Remove** the roll by changing `@` to `.` at those coordinates
   - Update the `paper_map`

2. **Repeat** the Part 1 logic on the updated `paper_map`
   - Continue removing rolls until no more can be removed
   - Each removal may expose new rolls that now have fewer than 4 neighbors

3. **Output**: Print the total number of rolls that can be removed after more rolls have been removed

### Example:

**Initial Grid:**

```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

```

**After 37 Removals:**
```
..........
..x.......
.x@@@.....
..@@@@....
...@@@@...
..x@@@@@..
...@.@.@@.
..x@@.@@@x
...@@@@@@.
....@@@...
```

**Final Output**
````
..........
..........
..........
...x@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
````
---

This day's solution can be further optimized and be made into a single function, but with some testing I found suboptimal, long run times even with smaller sized inputs. This can be a revision for another day