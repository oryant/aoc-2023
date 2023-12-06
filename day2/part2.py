import os
from typing import Tuple


def split_line(line: str) -> Tuple[int, list]:
    splitline = line.split(":")
    return (
        int(splitline[0].split()[1]),
        [tuple(x.split()) for x in ",".join(splitline[1].split(";")).split(",")],
    )


def get_balls(line: list[Tuple], colour: str) -> int:
    return max([int(x[0]) for x in line if x[1] == colour])


with open(os.path.join(os.getcwd(), "day2/input.txt")) as input_file:
    sum_balls = 0
    for line in input_file:
        splitline = split_line(line)
        sum_balls += (
            get_balls(splitline[1], "red")
            * get_balls(splitline[1], "green")
            * get_balls(splitline[1], "blue")
        )

print(sum_balls)
