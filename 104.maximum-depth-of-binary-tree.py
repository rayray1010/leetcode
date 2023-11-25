#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
from typing import Optional


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.find_depth(root, 0)

    def find_depth(self, root: Optional[TreeNode], depth: int):
        if not root:
            return depth
        return max(
            self.find_depth(root.left, depth + 1),
            self.find_depth(root.right, depth + 1),
        )


# @lc code=end


# [3,9,20,null,null,15,7]
a = Solution()
a.find_depth()
