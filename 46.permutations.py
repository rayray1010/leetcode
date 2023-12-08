# @before-stub-for-debug-begin
from python3problem46 import *
from typing import *
# @before-stub-for-debug-end

from typing import List, Set
#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            if len(path) > len(nums):
                return

            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                dfs(nums, path)
                path.pop()

        dfs(nums, [])
        return res


# @lc code=end
