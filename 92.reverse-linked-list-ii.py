from typing import Optional
#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(None, head)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        current = prev.next
        for _ in range(right - left):
            next = current.next
            current.next, next.next, prev.next = next.next, prev.next, next
        return dummy.next


# @lc code=end
