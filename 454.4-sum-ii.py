from collections import defaultdict
from typing import List
#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#


# @lc code=start
class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        nums_dict = defaultdict(int)

        for i in nums1:
            for j in nums2:
                nums_dict[i + j] += 1

        counter = 0

        for i in nums3:
            for j in nums4:
                counter += nums_dict[0 - i - j]
        return counter


# @lc code=end
