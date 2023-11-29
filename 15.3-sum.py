from typing import List
#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        p, n, zero = [], [], []

        for i in nums:
            if i > 0:
                p.append(i)
            if i < 0:
                n.append(i)
            if i == 0:
                zero.append(i)

        ans = set()
        N, P = set(n), set(p)

        if len(zero) >= 3:
            ans.add((0, 0, 0))

        if zero:
            for i in N:
                if -1 * i in P:
                    ans.add((i, 0, -1 * i))

        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                complement = -1 * (n[i] + n[j])
                if complement in P:
                    ans.add(tuple(sorted([n[i], n[j], complement])))

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                complement = -1 * (p[i] + p[j])
                if complement in N:
                    ans.add(tuple(sorted([p[i], p[j], complement])))

        return ans


# @lc code=end
