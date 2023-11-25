#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # To find next permutations, we'll start from the end
        i = j = len(nums) - 1
        # First we'll find the first non-increasing element starting from the end
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        # After completion of the first loop, there will be two cases
        # 1. Our i becomes zero (This will happen if the given array is sorted decreasingly). In this case, we'll simply reverse the sequence and will return
        if i == 0:
            nums.reverse()
            return
        # 2. If it's not zero then we'll find the first number grater then nums[i-1] starting from end
        while nums[j] <= nums[i - 1]:
            j -= 1
        # Now out pointer is pointing at two different positions
        # i. first non-assending number from end
        # j. first number greater than nums[i-1]

        # We'll swap these two numbers
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # We'll reverse a sequence strating from i to end
        nums[i:] = nums[len(nums) - 1 : i - 1 : -1]
        # We don't need to return anything as we've modified nums in-place
        """
            Dhruval
        """


# @lc code=end


def test_nextPermutation():
    solution = Solution()

    # Test case 1: Non-decreasing sequence
    nums = [1, 2, 3]
    solution.nextPermutation(nums)
    assert nums == [1, 3, 2]

    # Test case 2: Non-increasing sequence
    nums = [3, 2, 1]
    solution.nextPermutation(nums)
    assert nums == [1, 2, 3]

    # Test case 3: Random sequence
    nums = [1, 1, 5]
    solution.nextPermutation(nums)
    assert nums == [1, 5, 1]

    # Test case 4: Random sequence
    nums = [1, 3, 2]
    solution.nextPermutation(nums)
    assert nums == [2, 1, 3]

    # Test case 5: Random sequence
    nums = [2, 3, 1]
    solution.nextPermutation(nums)
    assert nums == [3, 1, 2]


test_nextPermutation()
