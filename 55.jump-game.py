# @before-stub-for-debug-begin
from python3problem55 import *
from typing import *
# @before-stub-for-debug-end

from typing import List
#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#


# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [False] * N
        dp[-1] = True

        for i in range(N - 1, -1, -1):
            if nums[i] == 0:
                continue

            for j in range(i + 1, min(i + nums[i], N - 1) + 1):
                if dp[j]:
                    dp[i] = True
                    break

        return dp[0]


# @lc code=end
