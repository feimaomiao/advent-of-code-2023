import typing

data = open("input.txt", "r").read().splitlines()


def a():
    s = 0
    for line in data:
        line = line.split(":")[1].split("|")
        winning_nums = [int(i) for i in line[0].split(" ") if i]
        ihave = [int(i) for i in line[1].split(" ") if i]
        l = len([i for i in winning_nums if i in ihave])
        if l:
            s += 2 ** (l - 1)
    print(s)


def b():
    s = 0
    count = [1 for i in range(len(data))]
    for index, line in enumerate(data):
        line = line.split(":")[1].split("|")
        winning_nums = [int(i) for i in line[0].split(" ") if i]
        ihave = [int(i) for i in line[1].split(" ") if i]
        l = len([i for i in winning_nums if i in ihave])
        for i in range(l):
            count[index + i + 1] += count[index]
    print(sum(count))


a()
b()
