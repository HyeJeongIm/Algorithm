import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, input().split(" ")))
# new_arr = []
sum_arr = [0]
result = 0
for num in arr:
  result += num
  sum_arr.append(result)

# print(sum_arr)

for _ in range(m):
  i, j = map(int, sys.stdin.readline().split())

  print( sum_arr[j] - sum_arr[i-1] )

  # 시간초과
  # new_arr = arr[i-1 : j]
  # print(sum(new_arr))

'''
5 3
5 4 3 2 1
1 3
2 4
5 5
'''
