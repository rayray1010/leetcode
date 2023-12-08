from typing import List, Optional
#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traversal(current_node, array):
            if not current_node:
                return

            traversal(current_node.left, array)
            array.append(current_node.val)
            traversal(current_node.right, array)

        traversal(root, res)
        return res


# @lc code=end
