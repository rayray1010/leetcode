from typing import List
#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        m_begin = n_begin = 0
        m_end, n_end = m - 1, n - 1
        ans = []

        while m_begin <= m_end and n_begin <= n_end:
            for i in range(n_begin, n_end + 1):
                ans.append(matrix[m_begin][i])
            m_begin += 1

            for i in range(m_begin, m_end + 1):
                ans.append(matrix[i][n_end])
            n_end -= 1

            if m_begin <= m_end:
                for i in range(n_end, n_begin - 1, -1):
                    ans.append(matrix[m_end][i])
                m_end -= 1

            if n_begin <= n_end:
                for i in range(m_end, m_begin - 1, -1):
                    ans.append(matrix[i][n_begin])
                n_begin += 1
        return ans


# @lc code=end
