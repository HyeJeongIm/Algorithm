'''
11:17 ~ 11:37
'''

num = input()
arr = list(map(int, num))
arr.sort()
result = 1

for i in range(1, len(arr)):

  if arr[i -1] == 0:
    result = 0
    result += arr[i]
  else: # 이전 값이 0이 아님

    # 현재 값을 곱해줌
    result *= arr[i]

print(result)


