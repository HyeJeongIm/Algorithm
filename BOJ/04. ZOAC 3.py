sl, sr = map(str, input().split(" "))
string = input()

keyboard1 = ['qwertyuiop',
            'asdfghjkl',
            'zxcvbnm']

keyboard = dict()

for x in range(3):
  for y in range(len(keyboard1[x])):
    keyboard[keyboard1[x][y]] = (x, y)

# print('keyboard1', keyboard1)
# print('keyboard', keyboard)

# 맨 처음 입력한 것의 위치
sl_x, sl_y = keyboard[sl]
sr_x, sr_y = keyboard[sr]

right = 'yuiophjklbnm'
result = 0

for ch in string: # z o a c
  nx, ny = keyboard[ch] # 현재 단어가 가리키는 위치 저장

  if ch in right:
    result += 1 + abs(sr_x - nx) + abs(sr_y - ny)
    # 이전 위치 현재로 update
    sr_x = nx
    sr_y = ny
  else:
    result += 1 + abs(sl_x - nx) + abs(sl_y - ny)
    # 이전 위치 현재로 update
    sl_x = nx
    sl_y = ny

print(result)

