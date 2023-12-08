from typing import List

#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#


# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        loop, mid = n // 2, n // 2
        start_x = 0
        start_y = 0
        counter = 1

        for offset in range(1, loop + 1):
            for i in range(start_y, n - offset):
                res[start_x][i] = counter
                counter += 1
            for i in range(start_x, n - offset):
                res[i][n - offset] = counter
                counter += 1
            for i in range(n - offset, start_y, -1):
                res[n - offset][i] = counter
                counter += 1
            for i in range(n - offset, start_x, -1):
                res[i][start_x] = counter
                counter += 1

            start_x += 1
            start_y += 1

        if n % 2 != 0:
            res[mid][mid] = counter

        return res


# @lc code=end
