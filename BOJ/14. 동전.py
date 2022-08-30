t = int(input())

for _ in range(t):

  coin_num = int(input()) # 동전의 가지 수
  arr = list(map(int, input().split()))
  arr.insert(0, 0)
  result = int(input())

  dp = [[0] * (result + 1) for i in range(coin_num + 1)] # 2차원 배열 생성

  for i in range(coin_num + 1):
    dp[i][0] = 1 # result = 0을 만들 수 있는 가지수는 무조건 1

  for j in range(1, coin_num + 1): # 화폐의 종류의 개수
    for i in range(1, result + 1): # 찾고자 하는 돈

      # j 행을 j-1행으로 update
      dp[j][i] = dp[j-1][i]

      # 4원짜리 동전으로는 4원부터 표현할 수 있습니다.
      # 이것을 체크하는 것
      if i - arr[j] >= 0:

        # j 값으로 표현할 수 있는 경우의 수를 더합니다.
        dp[j][i] += dp[j][i - arr[j]]

  print(dp[coin_num][result])






