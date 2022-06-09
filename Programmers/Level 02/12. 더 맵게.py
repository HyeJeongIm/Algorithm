import heapq

def solution(scoville, K):
  heapq.heapify(scoville)
  cnt = 0

  while True:
    min1 = heapq.heappop(scoville)

    if min1 >= K:
      break

    if len(scoville) < 1:
      return -1

    else:
      cnt += 1
      min2 = heapq.heappop(scoville)
      heapq.heappush(scoville, min1 + (min2 * 2))

  return cnt
