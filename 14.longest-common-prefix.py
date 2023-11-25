#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import List


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        v = sorted(strs)
        first = v[0]
        last = v[-1]
        ans = ""
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans


# @lc code=end

a = Solution()
a.longestCommonPrefix(["abcde", "abcge", "abced"])
