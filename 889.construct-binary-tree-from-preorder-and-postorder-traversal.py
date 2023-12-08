# @before-stub-for-debug-begin
from python3problem889 import *
from typing import *
# @before-stub-for-debug-end

from typing import Optional, List

#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.val_to_index = {}

    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        for i in range(len(postorder)):
            self.val_to_index[postorder[i]] = i
        return self.build(
            preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1
        )

    def build(
        self,
        pre_order: List[int],
        pre_start: int,
        pre_end: int,
        post_order: List[int],
        post_start: int,
        post_end: int,
    ) -> Optional[TreeNode]:
        if pre_start > pre_end:
            return None

        if pre_start == pre_end:
            return TreeNode(pre_order[pre_start])

        root_val = pre_order[pre_start]
        root = TreeNode(root_val)

        left_root_val = pre_order[pre_start + 1]
        left_root_idx = self.val_to_index[left_root_val]

        left_size = left_root_idx - post_start + 1

        root.left = self.build(
            pre_order,
            pre_start + 1,
            pre_start + left_size,
            post_order,
            post_start,
            left_root_idx,
        )

        root.right = self.build(
            pre_order,
            pre_start + left_size + 1,
            pre_end,
            post_order,
            left_root_idx + 1,
            post_end - 1,
        )
        return root


# @lc code=end
