from typing import List, Dict
import requests

data: List[str] = open("day1.txt", "r").readlines()
sub: Dict[str, str] = {
    "one": "o1ne",
    "two": "t2wo",
    "three": "t3hree",
    "four": "f4our",
    "five": "f5ive",
    "six": "s6ix",
    "seven": "s7even",
    "eight": "e8ight",
    "nine": "n9ine",
}


def calculate(flag: int) -> int:
    s: int = 0
    for i in data:
        if flag:
            for p in range(2):
                for r in sub:
                    i = i.replace(r, sub[r])
        st = "".join(k for k in i if k in "123456789")
        if st:
            m = int(st[0]) * 10 + int(st[-1])
            s += m
    return s


print(f"Run 1 {calculate(0)}")
print(f"Run 2 {calculate(1)}")
