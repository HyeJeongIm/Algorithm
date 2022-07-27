import itertools
import sys

n = int(input())
num = list(map(int, input().split()))
arr = list(map(int, input().split()))

op = [ '+', '-', '*', '/' ]
operator = []

for i in range(len(arr)): # 0, 1, 2, 3
  for j in range(arr[i]): # 2, 1, 1, 1
    operator.append(op[i])


arr1 = itertools.permutations(operator, len(operator))
arr_set = set(list(arr1)) # 가능한 연산자 모음

max = -sys.maxsize
min = sys.maxsize

for ope in arr_set:

  result = num[0]

  for i in range(len(ope)): # i = 0, 1, 2, 3, 4
    if ope[i] == '+':
      result += num[i+1]
    elif ope[i] == '-':
      result -= num[i+1]
    elif ope[i] == '*':
      result *= num[i+1]
    else:
      if result < 0:
        result = (result*(-1)) // num[i+1]
        result *= (-1)
      else:
        result //= (num[i+1])

  if result >= max:
    max = result
  if result < min:
    min = result

print(max)
print(min)




