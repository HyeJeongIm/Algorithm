def solution(numbers, target):
  answer = dfs(0, numbers, target)
  return answer


def dfs(result, numbers, target):
  if len(numbers) == 1:  # 개수가 한 개 인 경우
    if result + numbers[0] == target or result + numbers[0] == -target:
      return 1
    else:
      return 0
  else:
    return dfs(result + numbers[0], numbers[1:], target) \
           + dfs(result - numbers[0], numbers[1:], target)
