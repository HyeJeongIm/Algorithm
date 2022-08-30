import sys


class Solution:
  def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    min = sys.maxsize

    for k in range(2, len(nums)):
      i = 0
      j = k - 1

      while i < j:
        total = nums[i] + nums[j] + nums[k]

        if target == total:
          return target

        if abs(target - total) < min:
          min = abs(target - total)
          result = total

        if target > total:
          i += 1
        else:
          j -= 1

    return result
