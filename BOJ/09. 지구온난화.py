from sys import stdin
import copy

r, c = map(int, stdin.readline().split())

matrix = [list(input()) for _ in range(r)]

result = copy.deepcopy(matrix)

# 상하좌우 좌표
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


for y in range(r): # 행  0, 1, 2 ,3 , 4
  for x in range(c): # 열 0, 1, 2
    count = 0
    if matrix[y][x] == '.': # 바다
      continue

    # 땅 -> 주위 체
    for i in range(4):
      # x, y => 현재 위치
      ny = y + dy[i]
      nx = x + dx[i]

      # 범위 체크
      if 0 <= ny < r and 0 <= nx < c:
        # 바다확인
        if matrix[ny][nx] == '.':
          count += 1
      else:
        count += 1

    # 상하좌우 3개 이상이면 -> 현재 위치도 바다로 변함 (50년 뒤)
    if count >= 3:
      result[y][x] = '.'

start_y, end_y = 0, 0

for i in range(r):
  if 'X' in result[i]:
    start_y = i
    break
for i in range(r - 1, -1, -1):
  if 'X' in result[i]:
    end_y = i
    break

tmp = []
for j in range(c):
  for i in range(start_y, end_y + 1):

    if 'X' == result[i][j]:
      tmp.append(j)
      break

for y in range(start_y, end_y + 1):
  print("".join(result[y][tmp[0]:tmp[-1] + 1]))
