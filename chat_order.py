import sys

input = sys.stdin.readline

n = int(input())
"""
s = set()
chats = list()

for i in range(n):
    name = input()
    l = len(s)
    s.add(name)

    if l == len(s):
        chats.remove(name)
        chats.insert(0, name)
    else:
        chats.insert(0, name)

for chat in chats:
    print(chat.strip())
"""
s = set()
names = list()
for i in range(n):
    name = input()
    names.append(name)

for i in range(n-1, -1, -1):
    l = len(s)
    s.add(names[i])

    if l != len(s):
        print(names[i].strip())