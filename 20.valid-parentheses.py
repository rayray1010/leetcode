#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        s_map = {"(": ")", "{": "}", "[": "]"}

        if len(s) < 2:
            return False
        stack = []

        for i in s:
            if i in s_map:
                stack.append(i)
            elif len(stack) == 0 or s_map[stack.pop()] != i:
                return False
        return len(stack) == 0


# @lc code=end
