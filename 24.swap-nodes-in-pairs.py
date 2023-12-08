# @before-stub-for-debug-begin
from python3problem24 import *
from typing import *
# @before-stub-for-debug-end

from typing import Optional

#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev = head
        cur = head.next
        next = head.next.next

        cur.next = prev
        prev.next = self.swapPairs(next)
        return cur


# @lc code=end
