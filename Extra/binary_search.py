from typing import List


class Solution:
    """
    Initial Condition: left = 0, right = length-1
    Termination: left > right
    Searching Left: right = mid-1
    Searching Right: left = mid+1
    """

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            n = nums[mid]

            if target == n:
                return mid
            elif target < n:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def rotatedSearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # If the left half is not sorted, the right half must be sorted.
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Check if the peak is on the right side.
            if nums[mid] < nums[mid + 1]:
                left = mid + 1

            # Check if the peak is on the left side.
            else:
                right = mid

        return left

    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Check if the right side is unsortd.
            if nums[mid] > nums[right]:
                left = mid + 1

            else:
                right = mid
        return nums[left]


if __name__ == '__main__':
    list = [3, 3, 3, 3, 3, 3, 3, 1, 2, 1]

    sol = Solution().findPeakElement(list)
    print(sol)
