from tools import *
from sys import argv


def extrapolate(a: list):
    if len(a) < 2:
        return a
    if all(not i for i in a):
        return a
    new_a = extrapolate([a[i + 1] - a[i] for i in range(len(a) - 1)])
    a.append(a[-1] + new_a[-1])
    return a


def extrapolate_front(a: list):
    if len(a) < 2:
        return a
    if all(not i for i in a):
        return a
    new_a = extrapolate_front([a[i + 1] - a[i] for i in range(len(a) - 1)])
    a.insert(0, a[0] - new_a[0])
    return a


def a():
    data = open("input.txt").readlines()
    if len(argv) > 1:
        data = open("test.txt").readlines()
    s = 0
    for lines in data:
        s += extrapolate([int(i) for i in lines.split(" ") if i])[-1]
    print(s)


def b():
    data = open("input2.txt").readlines()
    if len(argv) > 1:
        data = open("test.txt").readlines()
    s = 0
    for lines in data:
        s += extrapolate_front([int(i) for i in lines.split(" ") if i])[0]
    print(s)


a()
b()
