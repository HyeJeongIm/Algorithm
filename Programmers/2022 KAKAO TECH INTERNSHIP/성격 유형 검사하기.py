'''
10:13 ~ 11:09
'''


def solution(survey, choices):
  dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
  arr = ["RT", "CF", "JM", "AN"]
  result = []

  for i in range(len(survey)):  # 0, 1, 2, 3, 4
    ch1 = survey[i][0]
    ch2 = survey[i][1]

    if choices[i] == 1:
      dic[ch1] = dic[ch1] + 3
    elif choices[i] == 2:
      dic[ch1] += 2
    elif choices[i] == 3:
      dic[ch1] += 1
    elif choices[i] == 4:
      pass
    elif choices[i] == 5:
      dic[ch2] += 1
    elif choices[i] == 6:
      dic[ch2] += 2
    elif choices[i] == 7:
      dic[ch2] += 3
    # print(i, dic)

  # 지표
  for j in range(len(arr)):  # 0, 1, 2, 3
    if dic[arr[j][0]] >= dic[arr[j][1]]:
      result.append(arr[j][0])
    else:
      result.append(arr[j][1])

  return "".join(result)

  # print(dic)

