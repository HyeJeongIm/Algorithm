'''
12:40 ~ 12:47
'''

n, k = map(int, input().split())
cnt = 0 # 횟수

while(True):

  if n % k == 0: # 나누어 떨어지면
    n = n // k
    cnt += 1

  else: # 나누어 떨어지지 않으면 -> 1 빼준다
    n = n - 1
    cnt += 1

  if n == 1:
    break

print(cnt)

