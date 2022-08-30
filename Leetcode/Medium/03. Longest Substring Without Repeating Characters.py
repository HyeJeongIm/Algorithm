'''

input: string
output: int

Q: 주어진 문자열에서 알파벳이 중복되지 않고 가장 길게 연속되는 문자열 일부를 반환하는 것
- 같은 알파벳이 있으면 안됨

'''

class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:

    if len(s) == 0:
      return 0

    if len(s) == 1:  # " "
      return 1

    arr_length = []  # 길이를 담을 배열

    for i in range(len(s)):  # 0, 1, 2, 3, 4, 5, 6, 7
      arr = []
      arr.append(s[i])

      if i == len(s) - 1:
        break
      else:
        for j in range(i + 1, len(s)):
          if s[j] not in arr:  # 중복되지 않는다면
            arr.append(s[j])
          else:  # 중복 된다면
            break
      print(arr)
      arr_length.append(len(arr))
      # print(arr_length)
    return max(arr_length)

