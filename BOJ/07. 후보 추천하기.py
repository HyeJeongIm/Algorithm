'''
2:54 ~
'''

n = int(input())
m = int(input())
arr = list(map(int, input().split()))

frame = []
cnt = []

for num in arr:
    if num in frame:
        cnt[frame.index(num)] += 1
    else:
        if len(frame) < n:
          frame.append(num)
          cnt.append(1)
        else:
          idx = cnt.index(min(cnt))
          del frame[idx]
          del cnt[idx]
          frame.append(num)
          cnt.append(1)

frame.sort()
print(' '.join(map(str, frame)))

'''
3
9
2 1 4 3 5 6 2 7 2
'''
