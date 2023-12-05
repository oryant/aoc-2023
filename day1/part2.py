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
    for number in NUMBERS:
        if number[0] in line:
            line_as_list[line.index(number[0])] = number[1]
    return [x for x in line_as_list if x.isdigit()][0]


def last(line: str) -> str:
    line_as_list = list(line)
    for number in NUMBERS:
        if number[0] in line:
            line_as_list[line.rindex(number[0])] = number[1]
    return [x for x in line_as_list if x.isdigit()][-1]


with open(os.path.join(os.getcwd(), "day1/input.txt")) as input_file:
    sum_lines = 0
    for line in input_file:
        sum_lines += int(first(line) + last(line))

print(sum_lines)
