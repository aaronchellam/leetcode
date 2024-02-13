from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # Perform binary search.
        while left <= right:
            mid = left + ((right - left) // 2)

            # If the target is found, return the index.
            if nums[mid] == target:
                return mid

            # If the target is smaller, search in the left half.
            elif target < nums[mid]:
                right = mid - 1

            # If the target is larger, search in the right half.
            else:
                left = mid + 1


        return left


if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,4,5]
    #nums = [1,2,4,5,6]
    target = 3
    print(sol.searchInsert(nums, target))