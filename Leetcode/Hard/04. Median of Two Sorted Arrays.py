'''
7:31 ~ 7:45

input: arr, arr
output: float

두 개의 arr 합치고
1) 홀수일 경우:
2) 짝수일 경우:

'''


class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    narr = nums1 + nums2
    narr.sort()

    arr_len = len(narr)
    index = arr_len // 2

    if arr_len % 2 == 0:  # 짝수
      return (narr[index - 1] + narr[index]) / 2


    else:  # 홀수
      return narr[index]
