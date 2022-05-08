def solution(people, limit):
  people.sort()  # 50, 50, 70, 80

  start = 0
  end = len(people) - 1
  cnt = 0

  while start <= end:

    sum = people[start] + people[end]

    if sum <= limit:
      start += 1
      end -= 1
    else:
      end -= 1

    cnt += 1

  return cnt
