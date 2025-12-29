# Day 2: Gift Shop

# ==========================
# Part 1
# ==========================
# Find each invalid ID from a list of number ranges according and adding them up for a final password
# to the following rules:
# 1. An invalid ID is a sequence of numbers that are repeated twice in sequence
    # Example:
    # 	55 (5 twice)
    # 	6464 (64 twice)
    # 	123123 (123 twice)
# 2. No numbers have leading zeroes
    #  Example:
    # 	0101 isn't an ID at all
    # 	but 101 is a valid ID that would be ignored in this filter

# in the range of 11-22, only 11 and 22 are the two invalid IDs
# in the range of 998-1012, only 1010 is an invalid ID
# in the range of 95 - 115, only 99 is an invalid ID
# Therefore by adding all the invalid IDs together: 
# 	11 + 22 + 1010 + 99
# 	1142 would be the correct solution in this example

#===========================
# Part 2
# ==========================
# Similarly to Part 1, Find each invalid ID from the number ranges, however, this time IDs are considered
# invalid only if some sequence of digits repeated at least twice. Once all the IDs are found, add them up for a final password.
# The same leading zero rule applies here as well.
# Example:
    # 12341234 (1234 two times)
    # 123123123 (123 three times)
    # 1212121212 (12 five times)
    # 1111111 (1 seven times) are all invalid IDs.

import re

totalIDsum = 0
totalSequenceSum = 0

def check_id(ID, check_type):
    global totalIDsum, totalSequenceSum

    if ID.startswith("0"):
        return False

    match check_type:
        case "IDvalidity":
            for i in range(1, len(ID) // 2 + 1):
                if ID[i:] == ID[:i]:
                    totalIDsum += int(ID)
                    return True
        case "sequence_validity":
            if re.match(r'^(.+?)\1+$', ID):
                totalSequenceSum += int(ID)
                return True
    return False

with open("input.txt", "r") as f:
    ranges_str = f.read().strip()
ranges = ranges_str.split(",")

for range_list in ranges:
    start, end = map(int, range_list.split("-"))
    for ID_num in range(start, end + 1):
        check_id(str(ID_num), "IDvalidity")
        check_id(str(ID_num), "sequence_validity")

print(f"\nFinal sum of all invalid IDs: {totalIDsum}")
print(f"Final sum of all invalid sequence IDs: {totalSequenceSum}")
