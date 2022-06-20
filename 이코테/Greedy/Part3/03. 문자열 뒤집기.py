'''
10:19 ~ 11:35
'''
# s = "0001100"
s = input()
s1 = list(map(int, s))
s2 = list(map(int, s))
cnt1 = 0 # 횟수
cnt2 = 0 # 횟수
result = 0

# case1 : 0으로 변경하는 경우
for i in range(1, len(s1)):

  # case1 : 0으로 변경하는 경우
  if s1[i-1] == 1:
    s1[i-1] = 0 # 0 으로 변경

    if s1[i] == 0:
      cnt1 += 1
    else: # 연속해서 1의 값을 갖는다면
      continue
  # print(cnt1, s1)


# case1 : 1으로 변경하는 경우
for j in range(len(s2) -1 ): # 0 1 2 3 4 5    6

  if s2[j] == s2[j + 1]: # 같은 숫자
    if s2[j] == 0: #00
      s2[j] = 1
    else: # 11
      continue

  else: # 01, 10
    cnt2 += 1
    if s2[j] == 0:
      s2[j] = 1
    else: # 10
      continue

result = min(cnt1, cnt2)
print(result)

  #
  # if arr[j] == 0:
  #   arr [j] = 1 # 0 으로 변경
  #   print(cnt2, arr)
  #
  #   if arr[j+1] == 1:
  #     cnt2 += 1
  #   else: # 연속해서 0의 값을 갖는다면
  #     continue
  # else:
  #   continue



# result = min(cnt1, cnt2)
# print(result)


