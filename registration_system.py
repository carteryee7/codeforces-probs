import sys

input = sys.stdin.readline

n = int(input())

lst = list()
s = set()
d = dict()

for i in range(n):
    a = input().strip()
    lst.append(a)

for name in lst:
    length = len(s)
    s.add(name)

    if length == len(s):
        new_name = name + str(d[name])
        s.add(new_name)
        d[name] += 1
        print(new_name)
    else:
        d[name] = 1
        print("OK")