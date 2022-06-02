'''
6:55 ~ 7:08
'''


def solution(s):
  dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

  word = ""
  result = []
  for i in s:
    if i.isdigit():  # 숫자면 바로 추가한다.
      result.append(i)
    else:
      word += i

      if word in dict:
        # print(word)
        # print(dict.get(word))
        result.append(str(dict.get(word)))
        word = ""

  return int("".join(result))
