# @before-stub-for-debug-begin
from python3problem106 import *
from typing import *
# @before-stub-for-debug-end

from typing import List, Optional
#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_dic = {value: index for index, value in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return None

            root = TreeNode(postorder.pop())

            mid_index = index_dic[root.val]

            root.right = helper(mid_index + 1, right)
            root.left = helper(left, mid_index - 1)

            return root

        return helper(0, len(inorder) - 1)


# @lc code=end
