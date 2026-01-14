# Day 5: Cafeteria

## Part 1: Counting Fresh Ingredients

### Overview

Given a list of fresh ingredient ID ranges and a list of available ingredient IDs, this day we have to found out how many of the available ingredient IDs are fresh. Logic being,any ID that falls inside a range is **fresh** otherwise it is considered **spoiled**. To make solving this easier, any overlapping ranges should be merged into one continuous range before counting by using recursion.

### Logic

**Input Format**
- Fresh ingredient ID ranges (one `start-end` pair per line)
- A blank line
- Available ingredient IDs (one ID per line)

**Process**
1. Read the ranges and the available IDs from the input.
2. Merge ranges that overlap or touch, keeping the lowest start and highest end for any combined range.
3. After merging, using binary search we find and count how many of the listed available IDs fall within any merged range.

**Range Merging Rules**
- If two ranges overlap or are contiguous, replace them with a single range that spans from the lowest start to the highest end.
- If a range is fully contained within another, keep only the larger outer range.

**Example merge:**
- Starting ranges: `(3-5), (10-14), (16-20), (12-18), (24-43), (29-39)`
- Merge `(16-20)` with `(12-18)` → `(12-20)`
- `(29-39)` is contained in `(24-43)` → keep `(24-43)`
- Final merged ranges: `(3-5), (10-20), (24-43)`

### Example
**Counting Fresh IDs:**

Available IDs: `1, 5, 8, 11, 17, 32`

- `1` → fresh (within `3-5`)
- `5` → not fresh (outside all ranges)
- `8` → not fresh (outside all ranges)
- `11` → fresh (within `10-20`)
- `17` → fresh (within `10-20`)
- `32` → fresh (within `24-43`)

**Result Total fresh IDs: 4**

So when comparing ranges like `48-64` and `50-92`, evaluate where each range extremity falls:
- `50` lies inside `48-64`
- `92` extends beyond `64`

Because the ranges overlap like this, we can merge the ranges into a single range giving us `48-92`.

---

## Part 2: Counting Total Fresh Ingredients

### Overview

Before determining which available IDs are fresh, this part calls for counting the total number of fresh ingredient IDs that exist within all the merged ranges. This represents the all of fresh ingredients available within the ranges, regardless of whether they appear in the available ID list in part 1. Surprisingly enough, with my approach to part 1, this second part's solution is a simple one line addition to the ``count_fresh`` function.

### Process
1. After merging all ranges, calculate the total count of consecutive IDs within each range.
2. For each range `(start-end)`, the count is `end - start + 1`.
3. Sum all range counts to get the total available fresh ingredients.

### Example
**Total Number of Fresh Ingredients**

Merged ranges: `29-34, 43-64, 72-86, 89-111`

- `29-34`: 6 IDs (29, 30, 31, 32, 33, 34)
- `43-64`: 22 IDs (43 through 64)
- `72-86`: 15 IDs (72 through 86)
- `89-111`: 23 IDs (89 through 111)

**Result: Total available fresh ingredients: 6 + 22 + 15 + 23 = 66**

