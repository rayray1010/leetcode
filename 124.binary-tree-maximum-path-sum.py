from typing import Optional, List

#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
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
        self.res = 0

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(root):
            if not root:
                return 0

            left_max = max(dfs(root.left), 0)
            right_max = max(dfs(root.right), 0)

            self.res = max(self.res, left_max + right_max + root.val)

            return root.val + max(left_max, right_max)

        dfs(root)
        return self.res


# @lc code=end
