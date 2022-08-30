class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:  # 0, 1, 2, 3, 4, 5

    results = []  # 정답을 담을 배열
    nums.sort()  # 기존 값 정렬

    for i in range(len(nums) - 2):  # 0, 1, 2, 3
      if i > 0 and nums[i] == nums[i - 1]:  # 값이 같으면
        continue

      left, right = i + 1, len(nums) - 1  # i = 1, left = 0, right = 5
      while left < right:  # 0 < 5
        sum = nums[i] + nums[left] + nums[right]  # 0, 1, 5
        if sum < 0:
          left += 1  # 0, 2, 5
        elif sum > 0:
          right -= 1  # 0, 2, 4
        else:
          results.append((nums[i], nums[left], nums[right]))  # 0이면 append

          while left < right and nums[left] == nums[left + 1]:
            left += 1
          while left < right and nums[right] == nums[right - 1]:
            right -= 1

          left += 1
          right -= 1

    return results
