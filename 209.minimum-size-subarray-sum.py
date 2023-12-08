# @before-stub-for-debug-begin
from python3problem209 import *
from typing import *
# @before-stub-for-debug-end

from typing import List

#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        l_pointer = r_pointer = 0
        min_length = float("inf")
        cur_sum = 0

        while r_pointer < length:
            cur_sum += nums[r_pointer]

            while cur_sum >= target:
                min_length = min(min_length, r_pointer - l_pointer + 1)

                cur_sum -= nums[l_pointer]
                l_pointer += 1

            r_pointer += 1

        return min_length if min_length != float("inf") else 0


# @lc code=end
