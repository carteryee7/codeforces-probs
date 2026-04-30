import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    maxes = [-1, -1]
    
    for i in range(n):
        if a[i] > maxes[0]:
            temp = maxes[0]
            maxes[0] = a[i]
            maxes[1] = temp
        elif a[i] > maxes[1] and a[i] != maxes[0]:
            maxes[1] = a[i]

    print(maxes[1])