'''
12:48 ~ 1:48
'''
# 배열의 크기, 더할 수 있는 횟수, 반복 가능한 횟수
N, M, K = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort(reverse = True)
point = 0
sum = 0
cnt = 0
total = 0

while(True):

  if total == M:
    break


  if cnt < K:
    if point == 1:
      cnt = 2

    cnt += 1
    total += 1
    sum += arr[point]
    # print(arr[point], sum, cnt, total)

  else:
    cnt = 0

    if point == 0:
      point += 1
    else:
      point -= 1
      # cnt = K - 1 이렇게하면 왜 안되는건지 모르겠음

print(sum)

'''
5 8 3
2 4 5 4 6
'''


