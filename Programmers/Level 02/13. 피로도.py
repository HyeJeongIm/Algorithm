from itertools import permutations


def solution(k, dungeons):
  result = 0

  for p in permutations(dungeons, len(dungeons)):
    tmp = k  # 주의
    cnt = 0

    for need, spend in p:
      if tmp >= need:
        # 가능
        tmp -= spend
        cnt += 1
    result = max(result, cnt)

  return result

