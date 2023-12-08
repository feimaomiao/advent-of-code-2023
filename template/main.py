from tools import *
from sys import argv


def a():
    data = open("input.txt").readlines()
    if len(argv) > 1:
        data = open("test.txt").readlines()


def b():
    data = open("input2.txt").readlines()
    if len(argv) > 1:
        data = open("test.txt").readlines()


a()
