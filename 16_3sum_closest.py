import numpy as np


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        def solver(nums, target, working_sum):
            if len(nums) == 1:
                x = nums[0]
                if (target >= 0 and x >= 0) or (target < 0 and x < 0):
                    return working_sum + x
                else:
                    return working_sum


