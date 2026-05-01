import sys
input = sys.stdin.readline

n = int(input())
a = list()
for _ in range(n):
    curr = input()
    a.append(curr)

s = set()

for name in a:
    length = len(s)
    s.add(name)

    if length == len(s):
        print("YES")
    else:
        print("NO")
