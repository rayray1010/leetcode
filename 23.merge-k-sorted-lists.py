# @before-stub-for-debug-begin
from python3problem23 import *
from typing import *
# @before-stub-for-debug-end

from typing import Optional, List
import heapq
#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        dummy = ListNode(None)
        dummy_pointer = dummy

        pq = []
        for i in lists:
            while i:
                heapq.heappush(pq, (i.val))
                i = i.next

        while pq:
            dummy_pointer.next = ListNode(heapq.heappop(pq))
            dummy_pointer = dummy_pointer.next

        return dummy.next


# @lc code=end
