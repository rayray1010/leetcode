from typing import Optional, List
from collections import deque
#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(root, max_val):
            if not root:
                return 0

            res = 1 if root.val >= max_val else 0

            res += dfs(root.left, max(root.val, max_val))
            res += dfs(root.right, max(root.val, max(root.val, max_val)))

            return res

        return dfs(root, root.val)


# @lc code=end
