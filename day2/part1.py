import os
from typing import Tuple

MAXIMA = {"red": 12, "green": 13, "blue": 14}
example = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"


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
            if int(pull[0]) > MAXIMA[pull[1]]:
                print(f"Bad game:{splitline[0]}, {pull[1]}, {pull[0]}")
                valid_line = False
                break
        sum_games += splitline[0] * valid_line

print(sum_games)
