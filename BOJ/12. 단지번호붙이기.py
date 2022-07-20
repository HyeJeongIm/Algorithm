from collections import deque

n = int(input())
graph = []

for _ in range(n):
  graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dan = 0
result = []

def bfs(i, j):

  # while 들어가기 전 첫 번째 좌표에 대한 처리 꼭 하기
  count = 1
  q = deque()
  q.append((i, j))
  graph[i][j] = 0

  while True:
    if len(q) == 0:
      break
    else:
      (x, y) = q.popleft()

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < n and 0<= ny < n:
          if graph[nx][ny] == 1:
            count += 1
            graph[nx][ny] = 0
            q.append((nx, ny))
  return count

for i in range(len(graph)):
  for j in range(len(graph[0])):
    if graph[i][j] == 1:
      dan += 1
      result.append(bfs(i, j))

print(dan)
result.sort()
for i in result:
  print(i)


'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
