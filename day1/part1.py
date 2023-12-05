import os

print(os.getcwd())

with open(os.path.join(os.getcwd(), "day1/input.txt")) as input_file:
    sum_lines = 0
    for line in input_file:
        digits = [x for x in line if x.isdigit()]
        sum_lines += int(digits[0] + digits[-1])

print(sum_lines)
