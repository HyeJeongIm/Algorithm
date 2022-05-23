def solution(left, right):
  sum = 0

  for num in range(left, right + 1):  # 13
    cnt = 0  # 약수의 개수

    for j in range(1, num + 1):

      # 약수체크
      if num % j == 0:
        cnt += 1
      else:  #
        continue

    if cnt % 2 == 0:  # 약수의 개수 -> 짝수
      sum += num
    else:  # 약수의 개수 -> 홀수
      sum -= num

  return sum
