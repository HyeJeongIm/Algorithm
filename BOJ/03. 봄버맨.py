from collections import deque

# 빈 곳에 폭탄을 설치해줍니다.
def make_bombs(graph):
  for i in range(r):
    for j in range(c):
      if graph[i][j] == '.':
        graph[i][j] = 'O'

# 폭탄을 발견합니다 -> 큐에 좌표를 추가해줍니다.
def find_bombs(graph):
  for i in range(r):
    for j in range(c):
      if graph[i][j] == 'O':
        q.append((i, j))

# 폭탄이 폭발합니다.
def del_bombs(graph):
  while q:
    x, y = q.popleft()
    graph[x][y] = '.' # 폭탄 파괴

    # 인접한 폭탄 파괴
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 범위 내에 존재하는지 체크
      if 0<= nx < r and 0 <= ny < c:
        graph[nx][ny] = '.'


if __name__ == "__main__":
  r, c, n = map(int, input().split())

  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]

  q = deque()

  graph = []
  for _ in range(r):
    graph.append(list(input().strip()))

  time = 1

  while time != n:


    find_bombs(graph)
    make_bombs(graph)
    time += 1

    if time == n:
      break

    del_bombs(graph)
    time += 1

  for result in graph:
    print("".join(result))



'''

6 7 3
.......
...O...
....O..
.......
OO.....
OO.....

--------

OOO.OOO
OO...OO
OOO...O
..OO.OO
...OOOO
...OOOO

'''

