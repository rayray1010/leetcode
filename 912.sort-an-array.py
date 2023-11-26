import random
from typing import List
#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#


# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort_helper(nums, 0, len(nums))
        return nums

    def quick_sort_helper(self, nums, lo, hi):
        if lo >= hi:
            return nums
        mid = self.partition(nums, lo, hi)
        self.quick_sort_helper(nums, lo, mid)
        self.quick_sort_helper(nums, mid + 1, hi)

    def partition(self, nums, lo, hi):
        p_index = random.randint(lo, hi - 1)
        nums[p_index], nums[hi - 1] = nums[hi - 1], nums[p_index]

        i = lo
        p = nums[hi - 1]
        for j in range(lo, hi - 1):
            if nums[j] < p:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[hi - 1] = nums[hi - 1], nums[i]
        return i


# @lc code=end
