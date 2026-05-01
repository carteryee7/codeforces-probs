import sys

input = sys.stdin.readline

nm = input().split()

n = int(nm[0])
m = int(nm[1])

ns = list()
ms = list()

ips = dict()
cmds = list()

for i in range(n):
    name_ip = input().split()
    ips[name_ip[1]] = name_ip[0]

for i in range(m):
    cmd = input().split()
    cmds.append(cmd)

for cmd in cmds:
    ip = cmd[1].replace(";", "")
    print(cmd[0] + " " + cmd[1] + " #" + ips[ip])
