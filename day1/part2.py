import os

print(os.getcwd())

NUMBERS = [
    ["five", "5"],
    ["one", "1"],
    ["eight", "8"],
    ["two", "2"],
    ["three", "3"],
    ["four", "4"],
    ["six", "6"],
    ["seven", "7"],
    ["nine", "9"],
]


def first(line: str) -> str:
    line_as_list = list(line)
    found_index = len(line)
    for number in NUMBERS:
        if number[0] in line:
            if line.index(number[0]) >= found_index:
                continue
            found_index = line.index(number[0])
            line_as_list[found_index] = number[1]
    return [x for x in line_as_list if x.isdigit()][0]


def last(line: str) -> str:
    line_as_list = list(line)
    found_index = 0
    for number in NUMBERS:
        if number[0] in line:
            if line.rindex(number[0]) <= found_index:
                continue
            found_index = line.rindex(number[0])
            line_as_list[found_index] = number[1]
    return [x for x in line_as_list if x.isdigit()][-1]


with open(os.path.join(os.getcwd(), "day1/input.txt")) as input_file:
    sum_lines = 0
    for line in input_file:
        sum_lines += int(first(line) + last(line))

print(sum_lines)
