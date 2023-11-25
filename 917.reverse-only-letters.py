#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#
# https://leetcode.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (63.51%)
# Likes:    2151
# Dislikes: 69
# Total Accepted:    190.8K
# Total Submissions: 300.5K
# Testcase Example:  '"ab-cd"'
#
# Given a string s, reverse the string according to the following rules:
#
#
# All the characters that are not English letters remain in the same
# position.
# All the English letters (lowercase or uppercase) should be reversed.
#
#
# Return s after reversing it.
#
#
# Example 1:
# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:
# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#
#
# Constraints:
#
#
# 1 <= s.length <= 100
# s consists of characters with ASCII values in the range [33, 122].
# s does not contain '\"' or '\\'.
#
#
#


# @lc code=start
# 解答
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letter_stack = [letter for letter in s if letter.isalpha()]
        ans = []
        for letter in s:
            if letter.isalpha():
                ans.append(letter_stack.pop())
            else:
                ans.append(letter)
        return "".join(ans)


# @lc code=end


# 自己寫的
# class Solution:
#     def reverseOnlyLetters(self, s: str) -> str:
#         s = list(s)
#         p_1 = 0
#         p_2 = len(s) - 1
#         while p_1 < p_2:
#             if s[p_1].isalpha() and s[p_2].isalpha():
#                 s[p_1], s[p_2] = s[p_2], s[p_1]
#                 p_1 += 1
#                 p_2 -= 1
#             elif s[p_1].isalpha():
#                 p_2 -= 1
#             elif s[p_2].isalpha():
#                 p_1 += 1
#             else:
#                 p_1 += 1
#                 p_2 -= 1
#         s = "".join(s)
#         return s
