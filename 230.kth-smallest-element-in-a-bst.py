# @before-stub-for-debug-begin
from python3problem230 import *
from typing import *
# @before-stub-for-debug-end

from typing import Optional, List

#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
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
        self.res = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def in_order(root, value_dic):
            if not root:
                return None

            if self.res:
                return

            in_order(root.left, value_dic)
            value_dic.append(root.val)
            if len(value_dic) == k:
                self.res = value_dic[-1]
                return
            in_order(root.right, value_dic)

        in_order(root, [])
        return self.res


# @lc code=end
