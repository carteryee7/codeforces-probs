import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    count = 0

    for i in range(n):
        for j in range(i+1, n):
            if nums[i] < i + 1 and nums[j] < j + 1 and i + 1 < nums[j]:
                count += 1
                #print("added")

    print(count)
