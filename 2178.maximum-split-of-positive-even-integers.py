from typing import List
#
# @lc app=leetcode id=2178 lang=python3
#
# [2178] Maximum Split of Positive Even Integers
#


# @lc code=start
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0 or finalSum < 2:
            return []
        ans, i = [], 2
        while i <= finalSum:
            ans.append(i)
            finalSum -= i
            i += 2
        ans[-1] += finalSum
        return ans


# @lc code=end
a = Solution()
print(a.maximumEvenSplit(12))
