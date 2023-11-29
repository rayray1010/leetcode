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
        heap = []
        dummy = ListNode(None)
        current = dummy
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        while heap:
            val, index = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next

            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))
                lists[index] = lists[index].next

        return dummy.next


# @lc code=end
