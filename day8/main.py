from re import match
from tools import *
from sys import argv
import itertools
import math


def a():
    data = open("input.txt").readlines()
    if len(argv) > 1:
        data = open("test.txt").readlines()
    sequence = data[0]
    nodes = {}
    for lines in data:
        m = match(r"([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)", lines)
        if not m:
            continue
        a, b, c = m.groups()
        nodes[a] = {0: b, 1: c}
    starting_node = nodes["AAA"]
    node_name = "AAA"
    count = 0
    for char in itertools.cycle(sequence):
        if node_name == "ZZZ":
            break
        if char not in "LR":
            continue
        if char == "L":
            starting_node = nodes[nodes[node_name][0]]
            node_name = nodes[node_name][0]
        elif char == "R":
            starting_node = nodes[nodes[node_name][1]]
            node_name = nodes[node_name][1]
        count += 1
    print(count)


def individual_node(m: str, nodes: dict, sequence) -> int:
    count = 0
    node = nodes[m]
    for char in itertools.cycle(sequence):
        print(node)
        print(m)
        print(char)
        if m.endswith("Z"):
            break
        if char not in "LR":
            continue
        if char == "L":
            m = node[0]
            node = nodes[m]
        elif char == "R":
            m = node[1]
            node = nodes[m]
        count += 1
    return count


def b():
    data = open("input.txt").readlines()
    if len(argv) > 1:
        data = open("test.txt").readlines()
    sequence = data[0]
    nodes = {}
    for lines in data:
        m = match(r"([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)", lines)
        if not m:
            continue
        a, b, c = m.groups()
        nodes[a] = {0: b, 1: c}
    list_starting_nodes = [i for i in nodes.keys() if i.endswith("A")]
    print(list_starting_nodes)
    l = []
    for i in list_starting_nodes:
        l.append(individual_node(i, nodes, sequence))
    print(math.lcm(*l))


a()
b()
