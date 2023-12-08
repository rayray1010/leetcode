from collections import defaultdict
from typing import List

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dic = defaultdict(int)

        for i, v in enumerate(nums):
            if target - v in nums_dic:
                return [nums_dic[target - v], i]
            nums_dic[v] = i
        return []


# @lc code=end
