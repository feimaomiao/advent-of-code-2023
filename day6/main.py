def combinations(k: int, target: int) -> int:
    c = 0
    for i in range(k):
        if i * (k - i) > target:
            c += 1
    return c


def a(test: bool = False):
    data = open("input.txt").readlines()
    if test:
        data = open("test.txt").readlines()
    times = [int(i) for i in data[0].split(":")[1].split(" ") if i]
    distance = [int(i) for i in data[1].split(":")[1].split(" ") if i]
    records = {}
    wins = 1
    for i in range(len(times)):
        # records[times[i]] = distance[i]
        wins *= combinations(times[i], distance[i])
    # for
    print(wins)


def b(test: bool = False):
    data = open("input2.txt").readlines()
    if test:
        data = open("test.txt").readlines()
        data = open("input.txt").readlines()
    if test:
        data = open("test.txt").readlines()
    times = [int(i) for i in data[0].split(":")[1].split(" ") if i]
    distance = [int(i) for i in data[1].split(":")[1].split(" ") if i]
    records = {}
    wins = 1
    for i in range(len(times)):
        # records[times[i]] = distance[i]
        wins *= combinations(times[i], distance[i])
    print(wins)


a()
b()
