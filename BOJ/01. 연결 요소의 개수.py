
from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n)] # 정점 개수만큼
check = [False] * n
cnt = 0


def bfs(j, arr, check):

  q = deque([j])
  check[j] = True # False -> True 로 변경

  while q:
    index = q.popleft()

    for i in arr[index]: # 1번에 연결된 번호 체크

      if check[i] == False:
        q.append(i)
        check[i] = True

for i in range(m):

  a, b = map(int, input().split())

  u = a-1
  v = b-1

  arr[u].append(v)
  arr[v].append(u)

for j in range(n): #

  if check[j] == False: # False
    cnt += 1 # 개수 증가
    bfs(j, arr, check) # index, 그래프, 방문여부

print(cnt)



'''
6 5
1 2
2 5
5 1
3 4
4 6
'''

'''
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
'''
