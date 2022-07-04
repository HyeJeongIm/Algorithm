from itertools import combinations

while True:
    num = list(map(int,input().split()))
    if num[0] == 0:
        break
    num.pop(0)
    arr = list(combinations(num,6))
    for result in arr:
        for i in range(len(result)):
            print(result[i],end=" ")
        print("")
    print("")
