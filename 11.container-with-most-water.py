from typing import List
#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        amount = 0
        while p1 < p2:
            amount = max((p2 - p1) * min(height[p1], height[p2]), amount)
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
        return amount


# @lc code=end
