'''
2:30 ~ 3:23

input: string
output: string

'''


class Solution:
  def longestPalindrome(self, s: str) -> str:

    for i in range(len(s)):  # i = 0
      arr = []
      arr.append(s[i])

      for j in range(i + 1, len(s)):  # j = 1, 2, 3

        i += 1  # i = 1

        if s[i] != s[j]:  # 01 12
          arr.append(s[j])  # cb
          print(arr)

          n_arr_len = len(arr)  # 현재 arr 길이 2
          na_arr_len = len(arr[j + 1:])  # 남은 arr 길이 2

          if n_arr_len > na_arr_len:  # 이건 비교 불가능함
            break
          else:
            for k in range(n_arr_len):  # 1 => 0 # 2 => 0, 1
              arr.append(s[k + i])  # s[3], s[4]
              # arr = cbbd

        else:  # 같다면
          result = []
          result.append(s[i])
          result.append(s[j])

          while (i == 0):

            i -= 1
            j += 1

            if s[i] != s[j]:
              break
            else:  # 같다면
              result.append(s[i])
              result.append(s[j])

    # return "".join(result)









