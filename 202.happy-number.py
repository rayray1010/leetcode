#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()
        while n not in record:
            record.add(n)
            new_sum = 0
            to_string = str(n)

            for i in to_string:
                new_sum += int(i) ** 2
            if new_sum == 1:
                return True
            n = new_sum
        return False


# @lc code=end
