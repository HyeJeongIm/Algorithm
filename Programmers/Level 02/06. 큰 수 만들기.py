def solution(number, k):
  stack = []

  for num in number:
    if len(stack) == 0:  # stack이 비어있는 경우, 무조건 추가
      stack.append(num)
      continue
    if k > 0:  # 제거할 수 있는 경우
      while stack[-1] < num:  # stack 값이 작은 경우 (pop, 개수)
        stack.pop()
        k -= 1

        if len(stack) == 0 or k <= 0:  # 계산을 하면서 1. stack이 비어있는경우, 2. 더이상 제거 불가능한 경우 -> 종료
          break
    stack.append(num)

  return "".join(stack[:len(stack) - k])
