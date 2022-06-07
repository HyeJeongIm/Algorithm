def solution(clothes):
  kind = {}
  cnt = 0  # 종류의 개수
  num = 1  # 조합의 개수

  for i in range(len(clothes)):
    if clothes[i][1] not in kind:
      cnt += 1
      kind[clothes[i][1]] = 1
    else:
      kind[clothes[i][1]] += 1

  if cnt == 1:
    return len(clothes)
  else:
    print(kind)
    for j in kind:
      print(kind[j])
      num *= (kind[j] + 1)
    return num - 1
