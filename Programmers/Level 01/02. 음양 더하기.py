def solution(absolutes, signs):
  sum = 0

  for i in range(len(signs)):
    if signs[i] == False:  # 'false' 이거 아님
      sum -= absolutes[i]
    else:
      sum += absolutes[i]

  return sum
