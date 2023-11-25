#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
from typing import List, Optional


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not len(nums):
            return None
        mid = len(nums) // 2
        mid_node = TreeNode(nums[mid])
        mid_node.left = self.sortedArrayToBST(nums[:mid])
        mid_node.right = self.sortedArrayToBST(nums[mid + 1 :])
        return mid_node


# @lc code=end
