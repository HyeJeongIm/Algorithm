def solution(progresses, speeds):
  stack = []
  result = []
  day = 0
  sum = 1

  for i in range(len(progresses)):
    speed = speeds[i]

    if (100 - progresses[i]) % speed == 0:
      day = (100 - progresses[i]) // speed
    else:
      day = ((100 - progresses[i]) // speed) + 1

    if len(stack) == 0:
      stack.append(day)
    else:  # day 비교
      if stack[-1] < day:
        result.append(sum)

        stack.append(day)
        sum = 1
      else:  # 10 5 이런경우
        sum += 1

  result.append(sum)
  return result
