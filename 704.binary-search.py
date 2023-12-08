# @before-stub-for-debug-begin
from python3problem704 import *
from typing import *
# @before-stub-for-debug-end

from typing import List
#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1


# @lc code=end


"""
記憶考點

兩種思維方式:
1. 左閉又開 [left, right)
    意思就是包含左邊但不包含右邊 
    [1, 2, 3, 4, 5] 取 [1,4) -- > [2, 3, 4]

2. 左閉右閉 [left, right]
    意思就是包含左右兩邊
    [1, 2, 3, 4, 5] 取 [1,4] -- > [2, 3, 4, 5]
"""
