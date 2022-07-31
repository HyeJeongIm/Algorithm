from collections import deque


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

# print(graph) # [[], [2, 3], [3, 4], [], []]

check = [-1] * (n + 1)
check[x] = 0

# 너비 우선 탐색(BFS) 수행
q = deque([x])
# print(q) # deque([1])

while q:
  now = q.popleft()
  # 현재 도시에서 이동할 수 있는 모든 도시를 확인
  for next_node in graph[now]:
    # 아직 방문하지 않은 도시라면
    if check[next_node] == -1:
      # 최단거리 갱신
      check[next_node] = check[now] + 1
      q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력

cnt = 0
for i in range(1, n + 1):
  if check[i] == k:
    print(i)
    cnt += 1

# 최단거리가 K인 도시가 없다면, -1 출력

if cnt == 0:
  print(-1)

'''
4 4 2 1
1 2
1 3
2 3
2 4

'''
