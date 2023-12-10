import re
from copy import copy


class nrange:
    def __init__(self, a, b):
        self.start = a
        self.stop = b
        self.valid = True

    def __str__(self):
        return f"NR{self.start, self.stop, int(self.valid)}"

    def __repr__(self):
        return str(self)


def a():
    list_seeds = [
        (int(i), False) for i in data.readline()[:-1].split(":")[1].split(" ") if i
    ]
    print(list_seeds)
    for l in data.readlines():
        c = False
        u = re.match(r"^(\d+) (\d+) (\d+)", l)
        k = re.match(r".+map\:.?", l)
        if not (u or k):
            continue
        if k:
            for i, s in enumerate(list_seeds):
                list_seeds[i] = (s[0], False)
            print(list_seeds)
            continue
        destination, source, length = (int(i) for i in u.groups())
        print(destination, source, length)
        for index, seeds in enumerate(list_seeds):
            if source <= seeds[0] <= source + length and not seeds[1]:
                print(f"Changing {seeds[0]} to {seeds[0] - source + destination}")
                list_seeds[index] = (seeds[0] - source + destination, True)
    print(min(i[0] for i in list_seeds))


def b():
    data1 = [int(i) for i in data.readline()[:-1].split(":")[1].split(" ") if i]
    list_seeds = [
        nrange(data1[i], data1[i] + data1[i + 1]) for i in range(0, len(data1), 2)
    ]
    group = []
    for l in data.readlines():
        c = False
        u = re.match(r"^(\d+) (\d+) (\d+)", l)
        k = re.match(r".+map\:", l)
        e = re.match(r".*\n$", l)
        if not (u or k):
            continue
        if u:
            group.append(tuple(int(i) for i in u.groups()))
            if e:
                continue
        if e and not k:
            continue
        ls_new = []
        for g in group:
            for s in list_seeds:
                if not s.valid:
                    continue
                if s.stop <= g[1] or s.start >= g[1] + g[2]:
                    continue
                if s.start < g[1]:
                    list_seeds.append(nrange(s.start, g[1]))
                    s.start = g[1]
                if s.stop > g[1] + g[2]:
                    list_seeds.append(nrange(g[1] + g[2], s.stop))
                    s.stop = g[1] + g[2]
                lower = s.start - g[1] + g[0]
                upper = s.stop - g[1] + g[0]
                shifted = nrange(lower, upper)
                ls_new.append(shifted)
                s.valid = False
        for s in list_seeds:
            if s.valid:
                ls_new.append(s)
        list_seeds = copy(ls_new)
        group = []

    print(min(i.start for i in list_seeds))


data = open("input.txt", "r")
a()
data = open("input.txt", "r")
b()
