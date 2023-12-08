from tools import *
from sys import argv
from collections import Counter


def sub(i: str):
    if i in "23456789":
        return int(i)
    return {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}[i]


def a():
    data = open("input.txt").readlines()
    if len(argv) > 1:
        data = open("test.txt").readlines()
    runs = []
    # s = 0
    for line in data:
        l = list(reversed(sorted([sub(i) for i in line.split(" ")[0]])))
        c = dict(Counter(l).items())
        pts = {6: 10, 9: 9, 8: 3, 5: 8, 4: 2, 0: 0, 7: 11}
        m = pts[sum(v + 2 for v in c.values() if v > 1)]
        order = [
            i
            for i, j in sorted(
                list(c.items()), key=lambda x: (x[1], x[0]), reverse=True
            )
            if j
        ]
        runs.append(
            (
                m,
                [sub(i) for i in line.split(" ")[0]],
                order,
                max(p for p, q in c.items() if q == max(c.values())),
                int(line.split(" ")[1]),
                l,
                line.split(" ")[0],
            )
        )
    runs.sort(key=lambda x: x[1])
    runs.sort(key=lambda x: x[0])
    s = 0
    for count, run in enumerate(runs):
        s += (count + 1) * run[4]
    print(s)


def b():
    data = open("input.txt").readlines()
    if len(argv) > 1:
        data = open("test.txt").readlines()
    runs = []
    for line in data:
        l = list(reversed(sorted([sub(i) for i in line.split(" ")[0]])))
        c = dict(Counter(l).items())
        items = list(reversed(sorted(list(c.items()), key=lambda x: (x[1], x[0]))))
        if items[0] != (1, 5):
            if items[0][0] != 1:
                c[items[0][0]] += c.get(1, 0)
            else:
                c[items[1][0]] += c.get(1, 0)
            if c.get(1, 0) > 0:
                del c[1]
        pts = {6: 10, 9: 9, 8: 3, 5: 8, 4: 2, 0: 0, 7: 11}
        m = pts[sum(v + 2 for v in c.values() if v > 1)]
        order = [
            i
            for i, j in sorted(
                list(c.items()), key=lambda x: (x[1], x[0]), reverse=True
            )
            if j
        ]
        runs.append(
            (
                m,
                [sub(i) for i in line.split(" ")[0]],
                int(line.split(" ")[1]),
                line.split(" ")[0],
            )
        )
    runs.sort(key=lambda x: x[1])
    runs.sort(key=lambda x: x[0])
    s = 0
    for count, run in enumerate(runs):
        s += (count + 1) * run[2]
    print(s)


a()
b()
