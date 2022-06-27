'''

n명의 수학점수가 주어집니다.
학생들의 평균을 구합니다. 평균에 가장 가까운 학생은 몇 번째 학생인가요?

'''

# n = int(input())

arr = [ 45, 73, 66, 87, 92, 67, 75, 79, 75, 80 ]
me = sum(arr) / len(arr)
me = round(me + 0.5)

# 평균이랑 가장 가까운 경우? ---> 나의 값 - 평균 의 값이 작은 것

sub_abs = abs(arr[0]  - me)

for i in range(1, len(arr)):

  check_abs = abs(arr[i] - me)

  if check_abs < sub_abs:

    sub_abs = check_abs
    score = arr[i]
    result1 = i

  elif check_abs == sub_abs:

    if score < arr[i]:
      score = arr[i]
      result1 = i

print( me , result1 + 1 ) # * 번째 학생을 묻고있음

