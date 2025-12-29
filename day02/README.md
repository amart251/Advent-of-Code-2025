# Two Different Approaches to Day 2 Part 1

## Approach One: Stack-Based Comparison

Checking the validity by splitting the ID into smaller growing chunks to compare every integer using stacks.

---

### Example 1: ID number 530830

**Sequence:** `5 → 3 → 0 → 8 → 3 → 0`

| Step | Action | Status |
|------|--------|--------|
| 1 | Read `5`, add to stack | Stack: `[5]` |
| 2 | Read `3`, no match, add to stack | Stack: `[5, 3]` |
| 3 | Read `53`, compare to `08`, no match, add to stack | Stack: `[5, 3, 0, 8]` |
| 4 | Only 2 numbers left, check for `[3, 0]` in stack | ✓ Not found |
| **Result** | **Valid ID** | ✓ |

---

### Example 2: ID number 25

**Sequence:** `2 → 5`

| Step | Action | Status |
|------|--------|--------|
| 1 | Read `2`, add to stack | Stack: `[2]` |
| 2 | Read `5`, no match, add to stack | Stack: `[2, 5]` |
| **Result** | **Valid ID** | ✓ |

---

### Example 3: ID number 123123123123

**Sequence:** `1 → 2 → 3 → 1 → 2 → 3 → 1 → 2 → 3 → 1 → 2 → 3`

| Step | Action | Stack Length | Remaining |
|------|--------|--------------|-----------|
| 1 | Read `1`, add to stack | 1 | 11 |
| 2 | Read `2`, add to stack | 2 | 10 |
| 3 | Read `31`, add to stack | 4 | 8 |
| 4 | Read `2312`, add to stack | 8 | 4 |
| 5 | Last 4 numbers: check if `[3, 1, 2, 3]` found in stack | — | — |
| **Result** | **Invalid ID** ✗ (Pattern found) | — | — |

---

## Approach Two: Palindrome Check ⭐ (Simpler Solution)

This task can be approached using a classic palindrome problem (which I don't know why I didn't think of using to begin with). Since the instructions never specified that numbers had to be even or odd in length, a simple palindrome check can determine if the ID is valid or not, as long as there are no leading zeros in the number.

This is the simplest and correct approach compared to my inital stack-based approach.

# Part 2 Approach

## Using Regular Expressions

Since the same principal was used for this second part of the task, it was hard to figure out how to approach this without trying something else before trying to apply the logic of my first approach from part 1.

The problem with using that method is that there would be no simple way to "find the prefix" meaning the sequence without modifying that logic and chunking down the ID rather than building up. Of course it would yeild positive results if the sequence was made up of the same number (ie. 111 or 2222), but anything that was made of more than two numbers in sequence or was even in length, the logic would eventually become too spread out and complex.

Figuring out how to apply the logic needed with regular expressions became the more appealing approach to find these patterns. Simple enough, it yeilded the correct result. To combine the two logics, I opted to use a switch case since for some reason the sums either "split" between the two output values, ignored one the conditional over the other, or not cover all the invalid IDs entirely.