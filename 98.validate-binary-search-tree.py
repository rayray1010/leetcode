from typing import Optional, List

#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def validate(root, left, right):
            if not root:
                return True
            if root.val <= left or root.val >= right:
                return False

            return validate(root.left, left, root.val) and validate(
                root.right, root.val, right
            )

        return validate(root, float("-inf"), float("inf"))


# @lc code=end
