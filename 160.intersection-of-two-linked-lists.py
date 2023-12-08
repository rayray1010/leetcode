from typing import Optional

#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        def get_length(head):
            if not head:
                return 0
            counter = 0
            while head:
                counter += 1
                head = head.next
            return counter

        def move_forward(head, step):
            for i in range(step):
                head = head.next

            return head

        dis_betwee_a_b = get_length(headA) - get_length(headB)

        if dis_betwee_a_b > 0:
            headA = move_forward(headA, dis_betwee_a_b)
        else:
            headB = move_forward(headB, abs(dis_betwee_a_b))

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None


# @lc code=end
