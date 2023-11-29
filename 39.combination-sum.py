# @before-stub-for-debug-begin
from python3problem39 import *
from typing import *
# @before-stub-for-debug-end

from typing import List
#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#


# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def dfs(index, path, target, nums):
            if sum(path) == target:
                res.append(path)
                return
            if sum(path) > target:
                return

            for i in range(index, n):
                dfs(i, path + [nums[i]], target, nums)

        dfs(0, [], target, candidates)
        return res


# @lc code=end
