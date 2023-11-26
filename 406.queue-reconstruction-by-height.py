from typing import List
#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#


# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))

        result = []

        for person in people:
            result.insert(person[1], person)
        return result


# @lc code=end
