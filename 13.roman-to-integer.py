#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        roman_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        for i in s:
            ans += roman_dic[i]
        return ans


# @lc code=end
