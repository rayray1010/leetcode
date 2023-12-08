from typing import Optional, List

#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#


# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def remove_duplicate(nums, val):
            pointer = 0
            for i in range(len(nums)):
                if nums[i] != val:
                    nums[pointer] = nums[i]
                    pointer += 1
            return pointer

        p = remove_duplicate(nums, 0)
        for i in range(p, len(nums)):
            nums[i] = 0


# @lc code=end
