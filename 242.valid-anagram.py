#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_dic = {}
        for i in s:
            if i in str_dic:
                str_dic[i] += 1
            else:
                str_dic[i] = 1

        for i in t:
            if i not in str_dic:
                return False
            str_dic[i] -= 1

        for i in str_dic:
            if str_dic[i] != 0:
                return False
        return True


# @lc code=end
