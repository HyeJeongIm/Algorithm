# '-' 를 기준으로 구분합니다
arr = input().split('-')
# print(arr) # ['55', '50+40']

result1 = []

for arr1 in arr:

  sum1 = 0

  arr_num = list(map(int, arr1.split('+'))) # '+'를 기준으로 구분합니다.
  # print(arr_num)
  # [55]
  # [50, 40]

  sum1 = sum(arr_num)
  # print(sum1)
  # 55
  # 90

  result1.append(sum1)
  # print(result1)
  # [55]
  # [55, 90]


result = result1[0] * 2
for num in result1:
  result -= num

print(result)


