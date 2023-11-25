#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_arr = []
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit_arr.append(prices[i + 1] - prices[i])
        return sum(profit_arr)


# @lc code=end
