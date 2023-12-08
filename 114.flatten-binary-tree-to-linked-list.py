# @before-stub-for-debug-begin
from python3problem114 import *
from typing import *
# @before-stub-for-debug-end

from typing import Optional

#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        left = self.flatten(root.left)
        right = self.flatten(root.right)

        root.left = None
        root.right = left

        p = root
        while p.right:
            p = p.right
        p.right = right
        return root
        """
        Do not return anything, modify root in-place instead.
        """


# @lc code=end
