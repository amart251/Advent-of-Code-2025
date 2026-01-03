# Day 4: Printing Department


roll_counter = 0
post_removal_counter = 0
adjacent_offsets = [
        (-1, -1),  # top_left
        (0, -1),   # up
        (1, -1),   # top_right
        (-1, 0),   # left
        (1, 0),    # right
        (-1, 1),   # bot_left
        (0, 1),    # down
        (1, 1)     # bot_right
    ]


def paper_finder(paper_map):
    global roll_counter, adjacent_offsets, rows, cols

    valid_positions = []
    

    for y in range(rows):
        for x in range(cols):
            if paper_map[y][x] != "@":
                continue
            
            adjacent_rolls = 0
            
            for dx, dy in adjacent_offsets:
                adj_x = x + dx
                adj_y = y + dy
                
                if 0 <= adj_x < cols and 0 <= adj_y < rows:
                    if paper_map[adj_y][adj_x] == "@":
                        adjacent_rolls += 1
            
            if adjacent_rolls < 4:
                roll_counter += 1
                valid_positions.append((x, y, adjacent_rolls, paper_map[y][x]))
                
    
    return roll_counter, valid_positions


def paper_cleanup(paper_map):
    global post_removal_counter, adjacent_offsets, rows, cols

    while True:
        
        found_valid = False
        
        for y in range(rows):
            for x in range(cols):
                if paper_map[y][x] != "@":
                    continue
                
                adjacent_rolls = 0
                
                for dx, dy in adjacent_offsets:
                    adj_x = x + dx
                    adj_y = y + dy
                    
                    if 0 <= adj_x < cols and 0 <= adj_y < rows:
                        if paper_map[adj_y][adj_x] == "@":
                            adjacent_rolls += 1
                
                if adjacent_rolls < 4:
                    paper_map[y][x] = "."
                    post_removal_counter += 1
                    found_valid = True
                    break
            
            if found_valid:
                break
        
        if not found_valid:
            break
    
    return post_removal_counter


with open("input.txt", "r") as f:
    content = f.read().strip()
    paper_map = [list(row) for row in content.split("\n")]
    rows = len(paper_map)
    cols = len(paper_map[0]) if rows > 0 else 0

total_valid_rolls, _ = paper_finder(paper_map)
print(f"\nTotal number of accessable rolls of paper: {total_valid_rolls}")

total_removable_rolls = paper_cleanup(paper_map)
print(f"Total number of removable rolls of paper: {total_removable_rolls}")
