from tools import *
from sys import argv
import shapely


def xtoxy(x, h, v):
    return (x % h, x // h)


def xytox(x, y, h, v):
    return y * h + x


def maps(x, data, horizontal, vertical):
    curr_pipe = data[x]
    x, y = xtoxy(x, horizontal, vertical)
    mapping = {
        "|": ((x, y - 1), (x, y + 1)),
        "J": ((x - 1, y), (x, y - 1)),
        "7": ((x - 1, y), (x, y + 1)),
        "F": ((x + 1, y), (x, y + 1)),
        "L": ((x, y - 1), (x + 1, y)),
        "-": ((x - 1, y), (x + 1, y)),
    }
    return mapping[curr_pipe]


def a():
    data = open("input.txt").readlines()
    if len(argv) > 1:
        data = open("test.txt").readlines()
    horizontal = len(data[0]) - 1
    vertical = len(data)
    data = list("".join([i[:-1] for i in data]))
    curr_node = xtoxy(data.index("S"), horizontal, vertical)
    assert data[xytox(*curr_node, horizontal, vertical)] == "S"
    x, y = curr_node
    if x + 1 < horizontal and data[xytox(x + 1, y, horizontal, vertical)] in "-J7":
        next_node = xytox(x + 1, y, horizontal, vertical)
    elif y + 1 < vertical and data[xytox(x, y + 1, horizontal, vertical)] in "JL|":
        next_node = xytox(x, y + 1, horizontal, vertical)
    elif x - 1 >= 0 and data[xytox(x - 1, y)] in "LF-":
        next_node = xytox(x - 1, y, horizontal, vertical)
    else:
        next_node = xytox(x, y - 1, horizontal, vertical)
    curr_node = xytox(*curr_node, horizontal, vertical)
    count = 0
    while data[next_node] != "S":
        neighbor1, neighbor2 = maps(next_node, data, horizontal, vertical)
        # print(neighbor1, neighbor2, end="neighbors\n")
        neighbor1 = xytox(*neighbor1, horizontal, vertical)
        neighbor2 = xytox(*neighbor2, horizontal, vertical)
        if neighbor1 == curr_node:
            curr_node = next_node
            next_node = neighbor2
        else:
            curr_node = next_node
            next_node = neighbor1
        count += 1
    print((count + 1) / 2)


def b():
    # kek i cheated so hard
    data = open("input.txt").readlines()
    if len(argv) > 1:
        data = open("test.txt").readlines()
    horizontal = len(data[0]) - 1
    vertical = len(data)
    data = list("".join([i[:-1] for i in data]))
    curr_node = xtoxy(data.index("S"), horizontal, vertical)
    initial_index = curr_node
    x, y = curr_node
    flag = ""
    if x + 1 < horizontal and data[xytox(x + 1, y, horizontal, vertical)] in "-J7":
        next_node = xytox(x + 1, y, horizontal, vertical)
        flag = "R"
    elif y - 1 >= 0 and data[xytox(x, y - 1, horizontal, vertical)] in "JL|":
        flag = "D"
        next_node = xytox(x, y - 1, horizontal, vertical)
    elif x - 1 >= 0 and data[xytox(x - 1, y)] in "LF-":
        flag = "L"
        next_node = xytox(x - 1, y, horizontal, vertical)
    else:
        flag = "U"
        next_node = xytox(x, y + 1, horizontal, vertical)
    vertices = [curr_node]
    curr_node = xytox(*curr_node, horizontal, vertical)
    count = 0
    points = [curr_node]
    while data[next_node] != "S":
        neighbor1, neighbor2 = maps(next_node, data, horizontal, vertical)
        neighbor1 = xytox(*neighbor1, horizontal, vertical)
        neighbor2 = xytox(*neighbor2, horizontal, vertical)
        data[next_node] = "0"
        if neighbor1 == curr_node:
            curr_node = next_node
            next_node = neighbor2
        else:
            curr_node = next_node
            next_node = neighbor1
        count += 1
        points.append(curr_node)
        if data[next_node] in "JLF7":
            vertices.append(xtoxy(next_node, horizontal, vertical))
    polygon = shapely.geometry.polygon.Polygon(vertices)
    c = 0
    for i in range(vertical):
        for j in range(horizontal):
            p = xytox(j, i, horizontal, vertical)
            if p not in points:
                if polygon.contains(shapely.geometry.Point(j, i)):
                    c += 1
    print(c)


a()
b()
