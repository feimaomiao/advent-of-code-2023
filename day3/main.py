import typing
import re

data = list(open("input.txt").readlines())
symbolist = "1234567890..\n"
pattern = re.compile(r"(\d+)")
pattern2 = re.compile(r"\*")


def a():
    s = 0
    print(len(data[0]))
    for line, content in enumerate(data):
        # content = content
        intlist = re.finditer(pattern, content)
        for match in intlist:
            # try:
            #     print("RIGHT HERE " + match.group(1))
            #     quit()
            # except:
            #     pass
            span = match.span()
            added = False
            if line != 0:
                for i in data[line - 1][
                    span[0] - 1
                    if span[0] > 0
                    else span[0] : span[1] + 1
                    if span[1] + 1 < len(content)
                    else span[1]
                ]:
                    if i not in symbolist:
                        added = True
                        s += int(match.group(1))
                        break
            if added:
                continue
            if line != len(data) - 1:
                for i in data[line + 1][
                    span[0] - 1
                    if span[0] > 0
                    else span[0] : span[1] + 1
                    if span[1] + 1 < len(content)
                    else span[1]
                ]:
                    if i not in symbolist:
                        # print("case 2")
                        added = True
                        s += int(match.group(1))
                        # print(f"Adding {match.group(0)}")
                        break
            if added:
                continue
            if span[0] != 0:
                if content[span[0] - 1] not in symbolist:
                    added = True
                    # print("case 3")
                    s += int(match.group(1))
                    # print(f"Adding {match.group(0)}")
                    continue
            if added:
                continue
            if span[1] != len(content):
                if content[span[1]] not in symbolist:
                    added = True
                    s += int(match.group(1))
                    continue
    print(s)


def b():
    s = 0
    matches = []
    for line, content in enumerate(data):
        for match in re.finditer(pattern, content):
            matches.append((line, match))
    for line, content in enumerate(data):
        # print(line)
        starlist = re.finditer(pattern2, content)
        for match in starlist:
            adjacent = [
                i
                for i in matches
                if line - 1 <= i[0] <= line + 1
                and set(range(i[1].span()[0], i[1].span()[1])).intersection(
                    range(
                        match.span()[0] - 1 if match.span()[0] >= 2 else 0,
                        match.span()[1] + 1,
                    )
                )
            ]
            if adjacent:
                print(match)
                print(adjacent)
            if len(adjacent) == 2:
                s += int(adjacent[0][1].group(0)) * int(adjacent[1][1].group(0))
                print(adjacent)
    print(s)


a()
b()
