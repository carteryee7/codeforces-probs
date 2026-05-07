# ICPC World Finals 2025 Problem L

import sys

input = sys.stdin.readline

a = list(map(int, input().split()))

n = a[0]

start_y = a[2]
end_y = a[4]

distance = start_y - end_y

covered = 0

ys = []

for i in range(n):
    coords = list(map(int, input().split()))

    # adjust for coords outside end-pts
    y1 = min(coords[1], start_y)
    y1 = max(y1, end_y)
    y2 = max(coords[3], end_y)
    y2 = min(y2, start_y)

    # need to add sorting by y1 to prevent missing overlap count
    rect = [y2, y1]
    ys.append(rect)

    covered += (y2 - y1)

if end_y > start_y:
    print("0")
else:
    tot_diff = 0
    for i in range(len(ys) - 1):
        diff = ys[i][1] - ys[i+1][0]
        if diff > 0:
            diff = 0
        tot_diff += diff

    print(distance - (covered + tot_diff))
