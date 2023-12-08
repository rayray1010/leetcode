# @before-stub-for-debug-begin
from python3problem49 import *
from typing import *
# @before-stub-for-debug-end

from typing import List
#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dic = {}
        ans = []
        for _, word in enumerate(strs):
            sorted_word = "".join(sorted(word))
            if sorted_word in word_dic:
                word_dic[sorted_word].append(word)
            else:
                word_dic[sorted_word] = [word]

        for key in word_dic:
            ans.append(word_dic[key])
        return ans


# @lc code=end
