#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        matrix = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            matrix[i][i] = True
            longest_palindrome = s[i]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if matrix[i + 1][j - 1] is True or j - i == 1:
                        matrix[i][j] = True
                        if len(longest_palindrome) < len(s[i : j + 1]):
                            longest_palindrome = s[i : j + 1]
        return longest_palindrome


# @lc code=end
