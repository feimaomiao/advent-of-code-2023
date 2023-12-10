from typing import *

data: List[str] = list(open("input.txt", "r").readlines())


def main1(red: int, green: int, blue: int) -> int:
    s: int = 0
    for lines in data:
        a: bool = True
        # format
        line_split = lines[:-1].split(": ")
        # parse game id
        game_id = int(line_split[0].split(" ")[1])
        # separate shows into
        for show in line_split[1].split("; "):
            showed = {"red": 0, "green": 0, "blue": 0}
            colors = show.split(", ")
            for c in colors:
                c = c.split(" ")
                showed[c[1]] += int(c[0])
            # check conditions
            if showed["red"] > red or showed["green"] > green or showed["blue"] > blue:
                a = False
                break
        # add game id
        if a:
            s += game_id
    return s


def main2() -> int:
    s = 0
    # parse lines
    for lines in data:
        colors_count = {"red": 0, "green": 0, "blue": 0}
        line_split = lines[:-1].split(": ")
        game_id = int(line_split[0].split(" ")[1])
        for show in line_split[1].split("; "):
            colors = show.split(", ")
            for c in colors:
                c = c.split(" ")
                # replace items
                if colors_count[c[1]] < int(c[0]):
                    colors_count[c[1]] = int(c[0])
        # add
        s += colors_count["red"] * colors_count["blue"] * colors_count["green"]
    return s


if __name__ == "__main__":
    print(f"Solution to part 1: {main1(12,13,14)}\nSolution to part 2: {main2()}")
