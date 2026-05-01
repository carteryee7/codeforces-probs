import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))
    
    heap = []  # max-heap (negate for Python's min-heap)
    total = 0
    
    for card in cards:
        if card > 0:
            heapq.heappush(heap, -card)
        else:
            # hero card
            if heap:
                total += -heapq.heappop(heap)
    
    print(total)