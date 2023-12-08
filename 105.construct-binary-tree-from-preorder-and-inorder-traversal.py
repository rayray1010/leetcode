# @before-stub-for-debug-begin
from python3problem105 import *
from typing import *
# @before-stub-for-debug-end

from typing import List, Optional
#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])

        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root


# @lc code=end


"""
之前解答
"""
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         inorder_dic = {inorder[i]: i for i in range(len(inorder))}

#         def helper(left, right):
#             if left > right:
#                 return None

#             root = TreeNode(preorder.pop(0))
#             mid_index = inorder_dic[root.val]

#             root.left = helper(left, mid_index - 1)
#             root.right = helper(mid_index + 1, right)

#             return root

#         return helper(0, len(preorder) - 1)
