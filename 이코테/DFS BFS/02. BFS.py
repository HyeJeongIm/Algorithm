from collections import deque

def bfs(graph, start, visited):

  q = deque([start])

  visited[start] = 1

  while q: # 큐가 빌 때까지 반복
    v = q.popleft()
    print(v, end = ' ')

    for i in graph[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = 1

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [0] * 9

bfs(graph, 1, visited)
