def solution(s):
  result = []

  for i in range(len(s)):

    # result 비어있는 경우
    if len(result) == 0:
      result.append(s[i])

    else:
      if s[i] == result[-1]:
        result.pop()
      else:
        result.append(s[i])

  if len(result) == 0:
    return 1
  else:
    return 0
