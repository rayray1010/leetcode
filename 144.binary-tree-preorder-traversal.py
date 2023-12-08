# @before-stub-for-debug-begin
from python3problem144 import *
from typing import *
# @before-stub-for-debug-end

from typing import List, Optional
#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traversal(current_node: Optional[TreeNode], res: List):
            if current_node is None:
                return
            res.append(current_node.val)
            traversal(current_node.left, res)
            traversal(current_node.right, res)
            return

        traversal(root, res)
        return res


# @lc code=end
