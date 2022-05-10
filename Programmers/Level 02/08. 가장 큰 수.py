def solution(numbers):
  numbers = list(map(str, numbers))

  numbers.sort(key=lambda x: x * 3, reverse=True)

  # input = [0, 0, 0, 0] 인 경우 -> "0000" 으로 return 된다
  # 따라서 int로 변환 후 다시 str로 변환
  return str(int("".join(numbers)))
