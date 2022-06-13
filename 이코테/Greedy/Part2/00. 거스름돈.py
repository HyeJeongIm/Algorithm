coin = [500, 100, 50, 10]
n = 1260

num = 0 # 동전의 개수

for c in coin:
  num += n // c
  n %= c

print(num)
  
