def solution(lottos, win_nums):
  result1 = 0
  cnt = 0  # 0의 개수

  for my in lottos:
    if my == 0:
      cnt += 1
    else:  # 0이 아닌 경우
      for check in win_nums:
        if my == check:
          result1 += 1
        else:  # 다르면
          continue

  if result1 == 6:
    rank = 1
  elif result1 == 5:
    rank = 2
  elif result1 == 4:
    rank = 3
  elif result1 == 3:
    rank = 4
  elif result1 == 2:
    rank = 5
  else:
    rank = 6

  # 등수 확인
  # 최고등수
  if cnt == 6:  # 0이 6개인 경우, 최고등수는 1순위
    max = 1
  else:
    max = rank - cnt
  # 최저등수
  min = rank

  result = [max, min]

  return result

