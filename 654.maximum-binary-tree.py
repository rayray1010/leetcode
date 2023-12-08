# @before-stub-for-debug-begin
from python3problem654 import *
from typing import *
# @before-stub-for-debug-end

from typing import Optional, List

#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums, lo, hi):
        # base case
        if lo > hi:
            return None

        max_val = max(nums[lo : hi + 1])
        max_index = nums.index(max_val)

        root = TreeNode(max_val)

        # 建構左右子樹
        root.left = self.build(nums, lo, max_index - 1)
        root.right = self.build(nums, max_index + 1, hi)

        return root


# @lc code=end
