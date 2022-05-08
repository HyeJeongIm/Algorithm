def solution(s):
  arr = list(map(int, s.split(" ")))

  arr.sort()
  string = str(arr[0]), str(arr[-1])

  return ' '.join(string)
