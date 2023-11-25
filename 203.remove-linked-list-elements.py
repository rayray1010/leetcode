#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_node = ListNode(None, head)
        current = dummy_node
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy_node.next


# @lc code=end

b = ListNode(5)
b.next = ListNode(2)
b.next.next = ListNode(2)
b.next.next.next = ListNode(4)
a = Solution()
a.removeElements(b, 2)
