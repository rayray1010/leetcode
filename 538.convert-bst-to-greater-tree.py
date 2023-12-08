from typing import Optional, List

#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0

        def dfs(node):
            if not node:
                return None

            dfs(node.right)

            self.sum += node.val
            node.val = self.sum
            dfs(node.left)
            return node

        return dfs(root)


# @lc code=end
