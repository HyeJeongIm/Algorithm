from collections import deque

n, m = map(int, input().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):

  q = deque()
  q.append((i, j))

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<= nx < n and 0<= ny < m:
        if graph[nx][ny] == 1:
          graph[nx][ny] = graph[x][y] + 1
          q.append((nx, ny))

      else:
        continue
  return graph[nx][ny]

for _ in range(n):
  arr = list(map(int, input()))
  graph.append(arr)



print(bfs(0, 0))

'''
5 6
101010
111111
000001
111111
111111
'''

