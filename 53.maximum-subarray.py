# @before-stub-for-debug-begin
from python3problem53 import *
from typing import *
# @before-stub-for-debug-end

from typing import List
#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


# @lc code=end
