from typing import List

#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#


# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_list = [0] * 26
        magazine_list = [0] * 26
        for i in ransomNote:
            ransom_list[ord(i) - ord("a")] += 1

        for i in magazine:
            magazine_list[ord(i) - ord("a")] += 1

        return all(ransom_list[i] <= magazine_list[i] for i in range(26))


# @lc code=end
