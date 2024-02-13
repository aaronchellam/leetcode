from typing import List


class Solution:
    def permute(self, nums: List) -> List[List]:
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]

                backtrack(start+1)

                nums[start], nums[i] = nums[i], nums[start]


        result = []
        backtrack(0)
        return result




if __name__ == '__main__':
    nums = ['A','B', 'C']
    result  = Solution().permute(nums)
    print(result)