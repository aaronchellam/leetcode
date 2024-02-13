from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # Store the complements in a map and return the corresponding index if a complement is found.
        map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in map:
                return [map[complement], i]
            else:
                map[num] = i

        return []


if __name__ == '__main__':
    sol = Solution()
    res = sol.twoSum2([2,7,11,15], 9)
    print(res)