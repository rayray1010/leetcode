#
# @lc app=leetcode id=935 lang=python3
#
# [935] Knight Dialer
#

# @lc code=start


class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        jump = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [0, 3, 9],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4],
        ]

        dp = [[0] * 10 for _ in range(n + 1)]
        for i in range(10):
            dp[0][i] = 1

        for i in range(1, n):
            for j in range(10):
                ans = 0
                for next_jump in jump[j]:
                    ans = (ans + dp[i - 1][next_jump]) % MOD
                dp[i][j] = ans
        ans = 0
        for i in range(10):
            ans = (ans + dp[n - 1][i]) % MOD
        return ans


# @lc code=end
