import heapq
import sys

N = int(input())
lheap = []
rheap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if len(lheap) == len(rheap):
        heapq.heappush(lheap,(-num,num))
    else:
        heapq.heappush(rheap,(num,num))
    
    if rheap and lheap[0][1] > rheap[0][1]:
        lval = heapq.heappop(lheap)[1]
        rval = heapq.heappop(rheap)[1]
        heapq.heappush(rheap,(lval,lval))
        heapq.heappush(lheap,(-rval,rval))
    print(lheap[0][1])
