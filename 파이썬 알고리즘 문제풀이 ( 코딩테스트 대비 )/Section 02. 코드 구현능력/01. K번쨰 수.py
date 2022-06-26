'''
3:12 ~

input: string
output: int

s, e 번째 까지의 수를 오름차순 정렬했을때, k번쨰로 나타나는 숫자를 출력하는 프로그램을 작성하세요

1번째 -> 0번 index
s번째 -> s-1번 index
'''

N = int(input())

for _ in range(N):
  n, s, e, k = map(int, input().split())
  num = list(map(int, input().split()))

  arr = num[s - 1: e]

  arr.sort()
  print(arr[k - 1])

