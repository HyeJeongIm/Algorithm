from itertools import permutations
import math


def solution(numbers):
  num = []
  result = 0

  for i in numbers:
    num.append(i)

  # numbers로 만들 수 있는 숫자 조합
  for i in range(1, len(numbers) + 1):  # 1, 2
    arr = set(list(permutations(num, i)))

    for j in arr:
      check_num = ''.join(j)

      if check_num[0] == '0':  # 011, 11은 같은 숫자로 취급해야 하는 case
        continue

      i = int(check_num)
      sum = 0

      for k in range(2, i):  # 7일때, 2 ~ 6 까지
        if i % k == 0:
          break
        else:
          sum += 1
      if sum == i - 2:
        result += 1  # 소수 체크

  return result
