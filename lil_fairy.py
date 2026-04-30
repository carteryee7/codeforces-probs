import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    s = set()
    
    i = 0
    c = 0
    while True:
        if i >= n:
            c = len(s)
            s.add(c)

            if c == len(s):
                break
        else:
            s.add(a[i])
        

        i += 1
    

    print(c)