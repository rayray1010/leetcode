from typing import List, Optional
#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traversal(current_node, array):
            if current_node is None:
                return
            traversal(current_node.left, array)
            traversal(current_node.right, array)
            array.append(current_node.val)

        traversal(root, res)
        return res


# @lc code=end
