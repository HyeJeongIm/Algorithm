def solution(A, B):
  A.sort()
  B.sort()

  sum = 0
  for i in range(len(A)):  # 0, 1, 2
    sum += A[i] * B[-1]
    B.pop()

  return sum
