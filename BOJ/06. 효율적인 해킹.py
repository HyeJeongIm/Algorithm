'''
12:21 ~
'''
# 효율적인 해킹
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x):
    q = deque()
    q.append(x) # 큐에 넣어 줍니다.

    visited = [False] * (N+1) # 초기화 해줍니다.
    visited[x] = True

    cnt = 1

    while q:
        node = q.popleft()
        for n in arr[node]:
            if not visited[n]: # 방문하지 않았으면
                q.append(n) # 큐에 넣어 줍니다.
                cnt += 1
                visited[n] = True
    return cnt

if __name__ == "__main__":
  N, M = map(int, input().split())
  arr = [[] for _ in range(N+1)] # [] 6개 생성

  for _ in range(M):
      a, b = map(int, input().split())
      arr[b].append(a)

  # print(arr) # [[], [3], [3], [4, 5], [], []]

  result = []
  for i in range(N+1): # i = 0, 1, 2, 3, 4, 5
      result.append(bfs(i))
  # print(result) # [1, 4, 4, 3, 1, 1]

  max_result = max(result)

  for i in range(1, N+1):
      if result[i] == max_result:
          print(i, end=' ')
