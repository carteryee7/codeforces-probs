import sys
import heapq

input = sys.stdin.readline

k = int(input())

nums = list(map(int, input().split()))

heap = []

# logic

"""
heapq.heapify(nums)

largest = heapq.nlargest(k, nums)

print(largest[-1])
"""

for num in nums:
    heapq.heappush(heap, -1 * num)

for _ in range(k-1):
    heapq.heappop(heap)

print(-1 * heapq.heappop(heap))