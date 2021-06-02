import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) >= 2:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            return answer
        else:
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville,min1+min2*2)
            answer += 1
    if scoville[0] > K:
        return answer
    else:
        return -1
      
      
      
#       heapq.heappush(heap, item) : item을 heap에 추가
#       heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨. 
#       heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
