from typing import List

#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#


# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, i = 0, len(nums) - 1, len(nums) - 1
        result = [float("inf")] * len(nums)
        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:
                result[i] = nums[right] ** 2
                right -= 1
            else:
                result[i] = nums[left] ** 2
                left += 1
            i -= 1
        return result


# @lc code=end
