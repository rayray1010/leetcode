#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root or (root.left is None and root.right is None):
            return True
        if abs(self.findDepth(root.left, 0) - self.findDepth(root.right, 0)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def findDepth(self, root: Optional[TreeNode], depth: int):
        if not root:
            return depth

        return max(
            self.findDepth(root.left, depth + 1), self.findDepth(root.right, depth + 1)
        )


# @lc code=end

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.right.right = TreeNode(3)
tree.left.left.left = TreeNode(4)
tree.right.right.right = TreeNode(4)

solution = Solution()
print(solution.isBalanced(tree))  # Expected output: True
