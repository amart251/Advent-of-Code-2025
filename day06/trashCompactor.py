import re

import numpy as np


# Part 1
def calculate_column(col_index: int) -> int:
    numbers = [int(number_rows[row_idx][col_index]) for row_idx in range(len(number_rows))]
    operator = operators[col_index]
    
    def recursive_calculate(index: int, accumulator: int) -> int:
        if index == 0:
            return accumulator
        
        if operator == '*':
            return recursive_calculate(index - 1, numbers[index - 1] * accumulator)
        else:  # operator == '+'
            return recursive_calculate(index - 1, numbers[index - 1] + accumulator)
    
    return recursive_calculate(len(numbers) - 1, numbers[-1])

# Part 2
def calculate_matrix(col_index: int) -> int:
    col_values = [number_rows[row_idx][col_index] for row_idx in range(len(number_rows))]
    max_len = max(len(val) for val in col_values)
    col_values = [val.ljust(max_len) for val in col_values]
    
    matrix = np.array([list(val) for val in col_values])
    transposed = matrix.T
    
    numbers = []
    for col in transposed:
        number_str = ''.join(col).replace(' ', '')
        if number_str:
            numbers.append(int(number_str))
    
    operator = operators[col_index]
    
    def recursive_calculate(index: int, accumulator: int) -> int:
        if index == 0:
            return accumulator
    
        if operator == '*':
            return recursive_calculate(index - 1, numbers[index - 1] * accumulator)
        else:  # operator == '+'
            return recursive_calculate(index - 1, numbers[index - 1] + accumulator)
    
    return recursive_calculate(len(numbers) - 1, numbers[-1])


with open('input.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file.readlines()]

operator_line = lines[-1]
operator_positions = [i for i, char in enumerate(operator_line) if char in '*+']

number_rows = []
for line_idx in range(len(lines) - 1):
    line = lines[line_idx]
    row_data = []
    for col_idx, pos in enumerate(operator_positions):
        col_start = pos
        if col_idx < len(operator_positions) - 1:
            col_end = operator_positions[col_idx + 1]
        else:
            col_end = len(line)

        col_content = line[col_start:col_end].rstrip()
        row_data.append(col_content)
    
    number_rows.append(row_data)

operators = [operator_line[pos] for pos in operator_positions]

grand_total = 0
for col in range(len(operators)):
    column_result = calculate_column(col)
    grand_total += column_result
print(f"Part 1 - Grand total of all maths: {grand_total}")

cephalopod_total = 0
for col in range(len(operators)):
    column_result = calculate_matrix(col)
    cephalopod_total += column_result
print(f"Part 2 - Cephalopod math result: {cephalopod_total}")
