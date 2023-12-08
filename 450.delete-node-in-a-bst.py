from typing import Optional, List

#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(root: Optional[TreeNode], target: int):
            if not root:
                return None

            if root.val == target:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left

                if root.left and root.right:
                    right_side_min_node = min_node(root.right)
                    root.right = helper(root.right, right_side_min_node.val)

                    right_side_min_node.left = root.left
                    right_side_min_node.right = root.right
                    root = right_side_min_node

            if root.val > target:
                root.left = helper(root.left, target)
            if root.val < target:
                root.right = helper(root.right, target)

            return root

        def min_node(root):
            while root.left:
                root = root.left
            return root

        return helper(root, key)


# @lc code=end
