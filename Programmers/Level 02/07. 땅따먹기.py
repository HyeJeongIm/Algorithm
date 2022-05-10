def solution(land):
  result = land[0]
  for arr in land[1:]:
    print(arr)
    temp = [0, 0, 0, 0]
    for index, item in enumerate(arr):
      temp[index] = item + max(result[:index] + result[index + 1:])
    result = temp
  return max(result)
