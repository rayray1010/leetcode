from typing import List
#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#


# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # base case
        if sum(gas) - sum(cost) < 0:
            return -1

        gas_remain = 0
        start_index = 0
        for i in range(len(gas)):
            gas_remain += gas[i] - cost[i]
            if gas_remain < 0:
                start_index = i + 1
                gas_remain = 0
        return start_index


# @lc code=end

# base case
# if sum(gas) - sum(cost) < 0:
# 	return -1

# gas_tank = 0  # gas available in car till now
# start_index = 0  # Consider first gas station as starting point

# for i in range(len(gas)):

# 	gas_tank += gas[i] - cost[i]

# 	if gas_tank < 0:  # the car has deficit of petrol
# 		start_index = i+1  # change the starting point
# 		gas_tank = 0  # make the current gas to 0, as we will be starting again from next station

# return start_index
