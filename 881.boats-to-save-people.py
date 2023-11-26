from typing import List
#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#


# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats, high, lo = 0, len(people) - 1, 0
        while lo <= high:
            if people[lo] + people[high] <= limit:
                lo += 1
            boats += 1
            high -= 1
        return boats


# @lc code=end


def test_numRescueBoats():
    solution = Solution()

    # Test case 1: Example case
    people = [1, 2]
    limit = 3
    assert solution.numRescueBoats(people, limit) == 1

    # Test case 2: All people can fit in one boat
    people = [1, 2, 3, 4, 5]
    limit = 6
    assert solution.numRescueBoats(people, limit) == 3

    # Test case 3: Some people need to be in separate boats
    people = [1, 2, 3, 4, 5]
    limit = 4
    assert solution.numRescueBoats(people, limit) == 3

    # Test case 4: Empty list of people
    people = []
    limit = 5
    assert solution.numRescueBoats(people, limit) == 0

    # Test case 5: All people have the same weight
    people = [3, 3, 3, 3]
    limit = 5
    assert solution.numRescueBoats(people, limit) == 2

    print("All test cases pass")


test_numRescueBoats()
