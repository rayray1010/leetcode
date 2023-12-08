from typing import Optional, List

#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.mex_diameter_count = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.mex_diameter(root)
        return self.mex_diameter_count

    def mex_diameter(self, root):
        if not root:
            return 0

        left_max = self.mex_diameter(root.left)
        right_max = self.mex_diameter(root.right)

        self.mex_diameter_count = max(self.mex_diameter_count, left_max + right_max)

        return 1 + max(left_max, right_max)


# @lc code=end
