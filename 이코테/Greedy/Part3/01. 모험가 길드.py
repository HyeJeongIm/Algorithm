'''
12:15 ~ 12:30
'''

n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse = True)

point = 0
cnt = 0

while(True):

  if len(arr[point:]) == 0:
    break

  if len(arr[point:]) >= arr[point]:
    cnt += 1
    point += arr[point]

print(cnt)
