import os
from typing import Tuple

LIMITS = {"red": 12, "green": 13, "blue": 14}


def split_line(line: str) -> Tuple[int, list]:
    splitline = line.split(":")
    return (
        int(splitline[0].split()[1]),
        [tuple(x.split()) for x in ",".join(splitline[1].split(";")).split(",")],
    )


with open(os.path.join(os.getcwd(), "day2/input.txt")) as input_file:
    sum_games = 0
    for line in input_file:
        splitline = split_line(line)
        valid_line = True
        for pull in splitline[1]:
            if int(pull[0]) > LIMITS[pull[1]]:
                valid_line = False
                break
        sum_games += splitline[0] * valid_line

print(sum_games)
